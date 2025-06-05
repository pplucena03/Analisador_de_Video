import downloader.audio_downloader as ad

def main():
    url = input("Digite a URL: ")
    
    ad.download_audio(url)


if __name__ == "__main__":
    main()