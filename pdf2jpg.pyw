import sys
import os
import subprocess


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


PDFTOPPM = resource_path(os.path.join("bin", "pdftoppm.exe"))

files = sys.argv[1:]

pdfs = [
    f for f in files
    if os.path.isfile(f) and f.lower().endswith(".pdf")
]

for pdf in pdfs:
    base, _ = os.path.splitext(pdf)

    subprocess.run(
        [
            PDFTOPPM,
            "-jpeg",
            "-r", "300",
            pdf,
            base
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
