[Setup]
AppName=EasyClickConverter
AppVersion=1.0.0
AppPublisher=reeziel
AppPublisherURL=https://github.com/eimyaa
AppUpdatesURL=https://github.com/eimyaa/RCM-Converter-Standalone/releases/
DefaultDirName={pf}\RCM Converter
DisableProgramGroupPage=yes
UninstallDisplayIcon={app}\AudioToMP3.exe
Compression=lzma2/ultra
SolidCompression=yes
PrivilegesRequired=admin
OutputDir=output
OutputBaseFilename=EasyClickConverter v1.0 - Setup
WizardStyle=modern

[Files]
; EXEs
Source: "dist\AudioToMP3.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\VideoToMP4.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\VideoToMP3.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\VideoToWAV.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\ImagesToPDF.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\PDFToJPG.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\PDFToPNG.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\MOVToH264.exe"; DestDir: "{app}"; Flags: ignoreversion

; Shared binaries (ONCE)
Source: "bin\ffmpeg.exe"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: "bin\ffprobe.exe"; DestDir: "{app}\bin"; Flags: ignoreversion
; Poppler (ALL FILES)
Source: "bin\pdftoppm.exe"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: "bin\pdftocairo.exe"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: "bin\*.dll"; DestDir: "{app}\bin"; Flags: ignoreversion

[Registry]
; ===== ROOT MENU (CONTAINER ONLY) =====
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert"; ValueType: string; ValueName: "MUIVerb"; ValueData: "Convert with EasyClick"; Flags: uninsdeletekey
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert"; ValueType: string; ValueName: "SubCommands"; ValueData: ""

; ===== AUDIO =====
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\AudioToMP3"; ValueType: string; ValueName: "MUIVerb"; ValueData: "Audio → MP3"
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\AudioToMP3\command"; ValueType: string; ValueData: """{app}\AudioToMP3.exe"" ""%1"""

; ===== VIDEO =====
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\VideoToMP4"; ValueType: string; ValueName: "MUIVerb"; ValueData: "Video → MP4"
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\VideoToMP4\command"; ValueType: string; ValueData: """{app}\VideoToMP4.exe"" ""%1"""

Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\VideoToMP3"; ValueType: string; ValueName: "MUIVerb"; ValueData: "Video → MP3"
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\VideoToMP3\command"; ValueType: string; ValueData: """{app}\VideoToMP3.exe"" ""%1"""

Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\VideoToWAV"; ValueType: string; ValueName: "MUIVerb"; ValueData: "Video → WAV"
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\VideoToWAV\command"; ValueType: string; ValueData: """{app}\VideoToWAV.exe"" ""%1"""

; ===== IMAGES =====
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\ImagesToPDF"; ValueType: string; ValueName: "MUIVerb"; ValueData: "Images → PDF"
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\ImagesToPDF\command"; ValueType: string; ValueData: """{app}\ImagesToPDF.exe"" ""%1"""

; ===== PDF =====
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\PDFToJPG"; ValueType: string; ValueName: "MUIVerb"; ValueData: "PDF → JPG"
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\PDFToJPG\command"; ValueType: string; ValueData: """{app}\PDFToJPG.exe"" ""%1"""

Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\PDFToPNG"; ValueType: string; ValueName: "MUIVerb"; ValueData: "PDF → PNG"
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\PDFToPNG\command"; ValueType: string; ValueData: """{app}\PDFToPNG.exe"" ""%1"""

; ===== QUICKTIME =====
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\MOVToH264"; ValueType: string; ValueName: "MUIVerb"; ValueData: "QuickTime → H.264"
Root: HKCR; Subkey: "AllFilesystemObjects\shell\Convert\shell\MOVToH264\command"; ValueType: string; ValueData: """{app}\MOVToH264.exe"" ""%1"""


