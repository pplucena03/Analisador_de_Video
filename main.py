import downloader.audio_downloader as ad
import transcriber.transcribe as tr
import summarizer.summarize as su


def main():
    url = input("Digite a URL: ")
    
    audio_path = ad.download_audio(url)
    ad.converter_para_wav(audio_path, "outputs/audio/audio.wav")

    transcrição = tr.transcribe_audio(audio_path)

    resumo = su.summarize_text(transcrição)
    print(resumo)


if __name__ == "__main__":
    main()