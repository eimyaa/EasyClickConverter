import os
import sys
import subprocess

selected_files = sys.argv[1:]
# print("Selected files:", selected_files)

# Add to this list if found more video file formats
video_extensions = (
    '.mkv', '.mov', '.avi', '.wmv', '.flv', '.webm', '.mpeg', '.mpg', '.m4v', 
    '.3gp', '.3g2', '.ts', '.mts', '.m2ts', '.divx', '.vob', '.ogv', '.rm', 
    '.rmvb', '.asf', '.f4v', '.dv', '.drc', '.mxf', '.roq', '.viv', '.amv', 
    '.mp2', '.mpv', '.m2ts'
)
  
for file in selected_files:
    if os.path.isfile(file) and file.lower().endswith(video_extensions):
        print(file)
        base, ext = os.path.splitext(file)
        subprocess.run(['ffmpeg', '-i', f'{base+ext}', '-c:v', 'copy', f'{base}.mp4'])