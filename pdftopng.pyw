import os
import sys
import subprocess

selected_files = sys.argv[1:]

# Only PDF files
pdf_extensions = ('.pdf',)

for file in selected_files:
    if os.path.isfile(file) and file.lower().endswith(pdf_extensions):
        print(f"Converting {file} to PNG...")
        base, ext = os.path.splitext(file)
        subprocess.run(['pdftoppm', '-png', file, base])