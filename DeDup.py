import os
import subprocess
import configs
import FrameExtraction as frame
import shutil
from PIL import Image
import imagehash

def de_ffmpeg():
    print("Processing with FFMPEG DeDup:")
    if configs.image_extension ==".jpg":
        ffmpeg_command = f'ffmpeg -i "{configs.input_video}" -vf mpdecimate,setpts=N/FRAME_RATE/TB -vsync 0 -y -qmin 1 -qscale:v 1 "{configs.output_folder}"\\frame_%d"{configs.image_extension}"'
    elif configs.image_extension ==".png":
        ffmpeg_command = f'ffmpeg -i "{configs.input_video}" -vf mpdecimate,setpts=N/FRAME_RATE/TB -vsync 0 -y -qmin 1 -qscale:v 1 "{configs.output_folder}"\\frame_%d"{configs.image_extension}"'
    
    print("Removing The Duplicated Frames:")
    subprocess.call(ffmpeg_command, shell=False)
    
def de_imagehash():
    # Took a week break and I no longer understand how this works.
    print("Processing with Image Hashing DeDup:")
    for file_name in os.listdir(configs.output_temp):
        file_path = os.path.join(configs.output_temp, file_name)
        if os.path.isfile(file_path):
            shutil.copy(file_path, configs.output_temp)
    
    hash_size = configs.image_hash_treshhold
    image_hashes = {}
    for file_name in os.listdir(configs.output_folder):
        if not file_name.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
            continue
        
        file_path = os.path.join(configs.output_folder, file_name)
        with Image.open(file_path) as img:
            img_hash = str(imagehash.average_hash(img, hash_size=hash_size))
        
        if img_hash in image_hashes:
            print(f"Found a duplicate image: {file_name}")
            os.remove(file_path)
        else:
            image_hashes[img_hash] = file_name