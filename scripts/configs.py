import os

# Mainly a proof of concept, while it has speed optimization settings this won't be fast by nature cuz I use frame extraction instead of sum like vapoursynth
# General Settings
input_video = r"D:\input.mp4"
output_folder = r"D:\output" # automatically generated, no need to create the folder
num_threads = 24 # Number of Threads to utilize ( the more = better )
image_extension = ".jpg" # ".jpg" = higher speed lower quality, ".png" = Lower Speed, higher quality, u can probably leave it at .jpg
remove_temp = "false" # "true" or "false " - Remove temp folder

# Frame Extraction
frame_extraction_method = "cpu" # "cpu" or "cuda"

# DeDup Mode, false = No Dedup, ffmpeg = FFMPEG MP Decimation, hash = Image Hashing approach each with their own flaws
dedup_mode = "hash" # not 100% accurate
image_hash_treshhold = 16 # threshold of hashing, not an accuracy meter, recommended from 8-16

# DupBack Mode, Needs DeDup to work, basically dedups the images, upscales, then duplicates the upscales in order to not upscale unnecessary images, should boost the performance significantly.
dupback = "false" # "true" or "false", # only works with image hash

#Upscaler, false or realcugan
upscaler = "false" # not working

# RealCugan settings
scale = 2 # Output Scale (e.g 1920x1080 -> 3840x2160 )
model_path = r"D:\UpscalingScript\UpscalerScript\models\up2x-latest-denoise3x.pth"
half = True # FP16 or FP32 processing, True is indicated
tile = 0 # Tiling, lower the better, higher can allow upscaling on lower end gpus but tends to be slower
cache_mode = 0 # Lower the better for inference speed
device = "cuda:0" # Device number
nt = 2 # Number of processes, the higher the better, in high VRAM cases 2 or higher is indicated
n_gpu = 1 # Number of GPUs, leave to default
encode_params=['-crf', '21', '-preset', 'medium'] # FFMPEG params

# Makes an output temp, don't mess
separator = '\\'
output_temp = input_video.rsplit(separator,1)[0] + "\output_temp"


