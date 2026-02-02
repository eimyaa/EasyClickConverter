import os
import sys
import subprocess

selected_files = sys.argv[1:]
# print("Selected files:", selected_files)

# Add to this list if found more audio file formats
audio_extensions = (
    '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.aiff', '.opus', '.alac',
    '.mp2', '.mp1', '.mid', '.midi', '.amr', '.dsd', '.pcm', '.ape', '.au', 
    '.ra', '.tta'
)


for file in selected_files:
    if os.path.isfile(file) and file.lower().endswith(audio_extensions):
        print(file)
        base, ext = os.path.splitext(file)
        subprocess.run(['ffmpeg', '-i', f'{base+ext}', '-b:a', '192k', f'{base}.mp3'])