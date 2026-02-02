import os
import sys
import subprocess

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

FFMPEG_PATH = resource_path(os.path.join("bin", "ffmpeg.exe"))

selected_files = sys.argv[1:]

audio_extensions = (
    '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.aiff', '.opus', '.alac',
    '.mp2', '.mp1', '.mid', '.midi', '.amr', '.dsd', '.pcm', '.ape', '.au',
    '.ra', '.tta'
)

for file in selected_files:
    if os.path.isfile(file) and file.lower().endswith(audio_extensions):
        base, _ = os.path.splitext(file)
        output_file = f"{base}.mp3"

        try:
            subprocess.run(
                [
                    FFMPEG_PATH,
                    "-y",                 
                    "-i", file,
                    "-b:a", "192k",
                    output_file
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except subprocess.CalledProcessError:
            print(f"Failed to convert: {file}")
