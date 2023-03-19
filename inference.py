import configs
import scripts.FrameExtraction as frame
import scripts.DeDup as dedup
import scripts.Upscale as upscale
import scripts.Dupback as dupback
import sys
import os
import shutil

print("Processing Video/s:")

if not os.path.exists(configs.output_temp):
    os.mkdir(configs.output_temp)
if not os.path.exists(configs.output_folder):
    os.mkdir(configs.output_folder)

class FrameExtract():
    if configs.frame_extraction_method == "cpu":
        if configs.dupback != "false":
            sys.exit("You are supposed to run DeDup before Dupback")
        else:
            frame.extract_multithread()
    elif configs.frame_extraction_method == "cuda":
        pass
        # frame.cuda_extract()

class DeDuplication():
    if configs.dedup_mode == "ffmpeg":
        dedup.de_ffmpeg()
    elif configs.dedup_mode == "hash":
        dedup.de_imagehash()

class Upscaling():
    if configs.upscaler == "false":
        pass
    elif configs.upscaler == "realcugan":
        upscale.realcugan_upscale() # Needs Implementation
        
class DuplicateBack():
    if configs.dupback == "false":
        pass
    elif configs.dupback == "true":
        if configs.dedup_mode == "ffmpeg":
            sys.exit("You can't run dupback with ffmpeg, please refer to configs, this is a ffmpeg limitation")            
        else:
            dupback.dupback()
match configs.remove_temp:
    case "true":
        shutil.rmtree(configs.output_temp)
    case "false":
        pass
