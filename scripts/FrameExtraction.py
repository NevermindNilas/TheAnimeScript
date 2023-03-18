import cv2
import os
import threading
import configs
import cupy as cp
import numpy as np

input_video = configs.input_video
num_threads = configs.num_threads
    
def extract_frames(start_frame, end_frame):
    video = cv2.VideoCapture(input_video)
    video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    i = start_frame
    while(i < end_frame and video.isOpened()):
        ret, frame = video.read()
        if ret == False:
            break
        cv2.imwrite(os.path.join(configs.output_temp, 'frame_' + str(i) + configs.image_extension), frame)
        i += 1
    video.release()

def extract_multithread():
    video = cv2.VideoCapture(input_video)
    num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_per_thread = num_frames // num_threads
    threads = []
    for i in range(num_threads):
        start_frame = i * frames_per_thread
        end_frame = (i+1) * frames_per_thread if i < num_threads-1 else num_frames
        thread = threading.Thread(target=extract_frames, args=(start_frame, end_frame))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
        
def cuda_extract():
    
    # Written with ChatGPT, still brokey, will figure this one out one day but it's technically much much much faster
    with open(input_video, "rb") as f:
        video_data = f.read()
    cap = cv2.VideoCapture(input_video)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    num_streams = cp.cuda.runtime.getDeviceCount()
    streams = [cp.cuda.Stream() for _ in range(num_streams)]
    d_video = cp.frombuffer(video_data, dtype=np.uint8).reshape((num_frames, height, width, 3))

    d_frames = d_video.reshape((num_frames * height * width, 3))
    d_output = cp.zeros((num_frames, height, width, 3), dtype=np.uint8)

    chunk_size = num_frames // num_streams
    for i in range(num_streams):
        start = i * chunk_size
        end = start + chunk_size if i < num_streams - 1 else num_frames
        with streams[i]:
            cp.ElementwiseKernel(
                "raw T video, raw int32 dim",
                "raw T output",
                """
                int i = i1 / (dim.y * dim.z);
                int j = (i1 / dim.z) % dim.y;
                int k = i1 % dim.z;
                output[i][j][k][0] = video[i * dim.y * dim.z + j * dim.z + k][0];
                output[i][j][k][1] = video[i * dim.y * dim.z + j * dim.z + k][1];
                output[i][j][k][2] = video[i * dim.y * dim.z + j * dim.z + k][2];
                """,
                "frame_extractor"
            )(d_video[start:end], (end - start, height, width, 3), d_output[start:end])
            
    h_frames = cp.asnumpy(d_output)
    
    for i in range(num_frames):
        frame = h_frames[i]
        frame_path = f"frame_{i}.png"
        # Write frame to file using OpenCV
        cv2.imwrite(frame_path, frame)