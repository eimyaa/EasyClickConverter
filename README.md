# EasyClickConverter

**EasyClickConverter** is a lightweight Windows right-click file conversion tool that lets you convert files instantly using the context menu — **no apps to open, no Python to install, no command line required**.

Right-click a file, choose **“Convert with EasyClick”**, and you’re done.

<img width="501" height="282" alt="eccdemooo" src="https://github.com/user-attachments/assets/ecf41fb9-c290-44d7-8a00-7e9f99093a8b" />

---

## Features

### Audio
- Audio → MP3  
- Video → MP3  
- Video → WAV  

### Video
- Video → MP4  
- QuickTime (`.mov`) → H.264 (`.mp4`)  
- HEVC (`.mkv`) → H.264 (`.mp4`)  

### PDF
- PDF → PNG  
- PDF → JPG  

### Images
- JPG / PNG → PDF (single or multi-page)
- HEIF → JPG 
- HEIF → PNG 

All conversions:
- Support **multiple selected files**
- Run **silently** in the background
- Output files next to the originals

---

##  How It Works

1. Install EasyClickConverter
2. Right-click any supported file
3. Click **Show more options** (Windows 11)
4. Select **Convert with EasyClick**
5. Choose the conversion you want

No windows. No popups. No setup after install.

---

##  What’s Included

EasyClickConverter is **fully standalone** and bundles everything it needs:

- FFmpeg (For Audio & Video conversion)
- Poppler (For PDF conversions)
- Embedded Python 3 Runtime (via PyInstaller)

 **Users do NOT need Python installed**

---

## System Requirements

- Windows 10 or Windows 11 (64-bit for now)
- Administrator privileges (For installation only)

---

## Supported Formats

**Input formats include (but are not limited to):**
- Audio: WAV, FLAC, AAC, M4A, OGG, WMA
- Video: MP4, MKV, AVI, MOV, WEBM
- Images: JPG, JPEG, PNG
- Documents: PDF

---

## Installation

1. Download the latest installer from **Releases**
2. Run the setup file
3. Follow the installation wizard
4. Right-click files to start converting

Uninstalling removes all context menu entries cleanly.

---

## Uninstall

- Open **Control Panel → Programs**
- Uninstall **EasyClickConverter**

No leftover registry entries.

---

## Why EasyClickConverter?

- Faster than opening full converter apps
- Cleaner than command-line tools
- Perfect for everyday conversions
- Privacy-friendly (100% local processing)

Designed to feel like a **native Windows feature**.

---

## Notes

- On Windows 11, custom context menu items appear under **Show more options**
- Image → PDF output name is based on the **first selected image**
- PDF → image conversions output one image per page

---

## License

EasyClickConverter is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

This project is free software: you can redistribute it and/or modify  
it under the terms of the GNU General Public License as published by  
the Free Software Foundation, either version 3 of the License, or  
(at your option) any later version.

This program is distributed in the hope that it will be useful,  
but **WITHOUT ANY WARRANTY**; without even the implied warranty of  
**MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE**.

---

## Credits

- **leconnn** — Original creator of  
  [Right-Click Menu Converter](https://github.com/leconnn/Right-Click-Menu-Converter),  
  which inspired and formed the base concept for this project

- FFmpeg  
- Poppler  
- Pillow  
- PyInstaller  
