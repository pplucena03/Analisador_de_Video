import downloader.audio_downloader as ad

def main():
    url = input("Digite a URL: ")
    
    audio_path = ad.download_audio(url)
    ad.converter_para_wav(audio_path, "outputs/audio/audio.wav")


if __name__ == "__main__":
    main()