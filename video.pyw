import os
import sys
import subprocess

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
    '.amv', '.mp2', '.mpv'
)

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

FFMPEG = resource_path(os.path.join("bin", "ffmpeg.exe"))

for file in selected_files:
    if not (os.path.isfile(file) and file.lower().endswith(video_extensions)):
        continue

    base, _ = os.path.splitext(file)
    output = base + ".mp4"

    cmd = [
        FFMPEG,
        "-y",
        "-i", file,

        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "20",
        "-pix_fmt", "yuv420p",

        # Audio: AAC
        "-c:a", "aac",
        "-b:a", "192k",

        # Metadata
        "-map_metadata", "0",
        "-movflags", "use_metadata_tags",

        output
    ]

    subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
