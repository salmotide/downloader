# SalmoDownloader

A Python-based music downloader project using yt-dlp and FFmpeg, with PySide6 planned for the desktop graphical interface.

This project is currently under development and focuses on learning Python, multimedia processing, and desktop application development.

## Technologies

- Python – Main programming language.
- yt-dlp – Media downloading library.
- FFmpeg – Audio and video processing.
- PySide6 – Desktop GUI framework.

## Project Structure

```text
SalmoDownloader/
├── .venv/
├── downloads/
├── main.py
├── downloader.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3.10 or newer.
- FFmpeg.
- pip.

## Installation

### 1. Clone the repository

```powershell
git clone git@github.com:salmotide/downloader.git 
cd SalmoDownloader
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Python dependencies

```powershell
pip install -r requirements.txt
```

### 5. Install FFmpeg

Make sure FFmpeg is installed and available in your system PATH.

Verify the installation:

```powershell
ffmpeg -version
```

## Current Development Status

- [x] Python environment setup.
- [x] Virtual environment setup.
- [x] Initial dependency selection.
- [ ] Implement audio downloader.
- [ ] Integrate FFmpeg audio conversion.
- [ ] Create desktop interface using PySide6.
- [ ] Add download progress tracking.
- [ ] Add download history and settings.

## Usage

The application is currently under development. Download functionality has not yet been implemented.

## License

To be determined.
