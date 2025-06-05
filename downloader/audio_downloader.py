import yt_dlp, subprocess, os

FFMPEG_PATH = r'C:\ffmpeg-7.1.1-full_build\bin'

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'outputs/audio/%(title)s.%(ext)s', 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': True,
        'ffmpeg_location': FFMPEG_PATH,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        
        try:
            filename = info['requested_downloads'][0]['filepath']
            filename = filename.rsplit(".", 1)[0] + ".mp3"

        except (KeyError, IndexError):
            filename = ydl.prepare_filename(info)
            filename = filename.rsplit(".", 1)[0] + ".mp3"

    return filename

def converter_para_wav(input_path: str, output_path: str):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {input_path}")

    comando = [
        "ffmpeg",
        "-i", input_path,
        "-ar", "16000",
        "-ac", "1",
        "-c:a", "pcm_s16le",
        output_path
    ]
    subprocess.run([FFMPEG_PATH,'-i', input_path, output_path], check=True)