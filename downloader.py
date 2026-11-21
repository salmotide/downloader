import os
import yt_dlp

def download(url, folder, format_media):
    if not url:
        print("URL tidak boleh kosong")
        return False
    if not folder:
        print("Lokasi tidak boleh kosong")
        return False

    format_media = format_media.strip().lower()

    audio = ["mp3", "wav", "flac", "opus"]
    video = ["mp4", "mkv", "webm"]
    if format_media in audio:
        print("Mode Audio")
    elif format_media in video:
        print("Mode Video")
    else:
        print("Formatnya tidak mendukung")
        return False

    os.makedirs(folder, exist_ok=True)

    option = {
        "noplaylist": True,
        "outtmpl": os.path.join(folder, "%(title)s.%(ext)s"),
    }

    if format_media in audio:
        option.update({
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": format_media,
                    "preferredquality": "192",
                }
            ],
        })
    elif format_media in video:
        option.update({
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": format_media,
        })

    try:
        with yt_dlp.YoutubeDL(option) as downloader:
            downloader.download([url])
        return True
    except Exception as error:
        print(f"Download gagal: {error}")
        return False
