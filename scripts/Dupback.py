import os
import DeDup as dedup
import configs
import shutil

input_video = configs.input_video
output_folder = configs.output_folder
separator = '\\' # Don't mess with this plez, it can break stuff

def dupback():
    # Only works with Image Hash
    i = 0
    for file in output_folder:
        path_1 = output_folder + 'frame_' + str(i-1) + configs.image_extension
        path_2 = output_folder + 'frame_' + str(i) + configs.image_extension
        if not os.path.exists(path_2):
            shutil.copy(path_1)
        i += 1