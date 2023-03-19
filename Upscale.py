import configs
import subprocess
from upscalers import config as cugan
upscaler = configs.upscaler

def realcugan_upscale():
    cugan.input_dir = configs.input_video
    cugan.output_dir = configs.output_folder
    cugan.scale = configs.scale
    cugan.model_path2, cugan.model_path3, cugan.model_path4 = configs.model_path
    cugan.half = configs.half
    cugan.tile = configs.tile
    cugan.cache_mode = configs.cache_mode
    cugan.device = configs.device
    cugan.nt = configs.nt
    cugan.n_gpu = configs.n_gpu
    cugan.encode_params = configs.encode_params
    subprocess.call([r'D:\UpscalingScript\UpscalerScript\src\Cugan\go.bat'], shell=True)

        

           
