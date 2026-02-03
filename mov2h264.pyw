import sys
import os
import subprocess


def resource_path(relative_path):
    """ Get absolute path to resource (works with PyInstaller) """
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


FFMPEG = resource_path(os.path.join("bin", "ffmpeg.exe"))

files = sys.argv[1:]

mov_files = [
    f for f in files
    if os.path.isfile(f) and f.lower().endswith(".mov")
]

for mov in mov_files:
    base, _ = os.path.splitext(mov)
    output = base + "_h264.mp4"

    cmd = [
        FFMPEG,
        "-y",
        "-i", mov,
        "-vf",
        "zscale=transfer=linear,"
        "tonemap=hable,"
        "zscale=transfer=bt709,"
        "format=yuv420p",
        "-map_metadata", "0",
        "-movflags", "use_metadata_tags",

        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "20",

        "-c:a", "aac",
        "-b:a", "192k",
        output
    ]

    subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
