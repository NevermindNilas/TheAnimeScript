# TheAnimeScript:
The be all end all script for all anime editors ( and not only ).
This is still in super early development, expect frequent updates.

**Official Discord: https://discord.gg/CdRD9GwS8J**

# Installation:
## This Github page assumes:
	1. That you have FFMPEG installed in Path Variables ( if you want you use certain features ).
	2. That you have Python ( 3.10.6 or above ) & Git installed.
	3. That you have watched the Youtube Tutorial ( link coming soon ).

### Requirements:
	1.Download latest release
	2.Open a Terminal/Console inside the new folder & run:
	
	pip install -r .\requirements.txt
	
# Usage:
	1. In Folder, Scripts, open config.py and modify to your needs.
	2. After, open a terminal inside Scripts and run:
	
	python inference.py

# Known Issues:
	1. The process runs twice, no clue why but I will figure it somehow out.
	2. Can't upscale yet, it will be soon added, for now it's only dedup and dupback.
	3. Very ugly code ( can't do much about it, I can barely read )

# Coming Features:
	**not in a specific order**
	1. Upscaling with Real-Cugan and Real-ESRGan
	2. Cuda Accelerated Frame Extraction.
	3. Vapoursynth ( no more need for Frame Extraction ).
	4. Prebuilt Build, no more need for downloading requirements and ffmpeg and what not.
	5. Batch Processing instead of single input.
	6. Verbose Client Interface instead of Config.py approach ( much easier for the average person )
	
