import os
import sys
import subprocess


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

PDFTOPPM_PATH = resource_path(os.path.join("bin", "pdftoppm.exe"))

selected_files = sys.argv[1:]

pdf_extensions = ('.pdf',)

for file in selected_files:
    if os.path.isfile(file) and file.lower().endswith(pdf_extensions):
        base, _ = os.path.splitext(file)

        try:
            subprocess.run(
                [
                    PDFTOPPM_PATH,
                    "-png",
                    file,
                    base
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except subprocess.CalledProcessError:
            print(f"Failed to convert: {file}")
