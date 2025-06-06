import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("turbo")

    try:
        result = model.transcribe(audio_path)

    except Exception as e:
        print(f"Erro ao transcrever o áudio: {e}")
        return False

    return result