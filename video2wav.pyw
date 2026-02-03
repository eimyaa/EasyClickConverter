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

video_extensions = (
    '.mkv', '.mov', '.avi', '.wmv', '.flv', '.webm',
    '.mpeg', '.mpg', '.m4v',
    '.3gp', '.3g2',
    '.ts', '.mts', '.m2ts',
    '.divx', '.vob', '.ogv',
    '.rm', '.rmvb', '.asf',
    '.f4v', '.dv', '.drc',
    '.mxf', '.roq', '.viv',
    '.amv', '.mp2', '.mpv',
    '.mp4'
)

for file in selected_files:
    if not (os.path.isfile(file) and file.lower().endswith(video_extensions)):
        continue

    base, _ = os.path.splitext(file)
    output_file = base + ".wav"

    try:
        subprocess.run(
            [
                FFMPEG_PATH,
                "-y",
                "-i", file,

                "-vn",
                "-map", "a:0",

                "-acodec", "pcm_s16le",
                "-ar", "44100",
                "-ac", "2",

                output_file
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError:

        pass
