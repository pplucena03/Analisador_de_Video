# 🎮 Analisador de Vídeos com IA

Este projeto utiliza inteligência artificial para analisar vídeos do YouTube, convertendo seu conteúdo em texto transcrito e resumido automaticamente.

---

## ⚙️ Funcionalidades

- 🔗 Baixa o áudio de qualquer vídeo do YouTube
- 🎧 Converte o áudio para `.wav` (mono, 16kHz)
- 🧠 Transcreve o áudio com Whisper
- 📝 Resume o conteúdo usando o GPT da OpenAI

---

## 📆 Tecnologias usadas

- [Python 3.11+](https://www.python.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) – para baixar o áudio
- [ffmpeg](https://ffmpeg.org/) – para conversão de áudio
- [Whisper](https://github.com/openai/whisper) – transcrição
- [OpenAI GPT API](https://platform.openai.com/docs) – sumarização
- [python-dotenv](https://pypi.org/project/python-dotenv/) – para lidar com a chave de API

---

## 🚀 Como rodar o projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/pplucena03/Analisador_de_Video.git
cd Analisador_de_Video
```

2. **Crie um ambiente virtual e ative-o:**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure sua chave da OpenAI:**

Crie um arquivo `.env` com:

```
OPENAI_API_KEY=sua-chave-aqui
```

5. **Execute o projeto:**

```bash
python main.py
```

---

## 📁 Estrutura do projeto

```bash
.
├── downloader/         # Baixa e converte o áudio
├── transcriber/        # Transcreve com Whisper
├── summarizer/         # Resume com GPT
├── outputs/            # Áudios e arquivos gerados
├── .env                # Chave da API (ignorado pelo Git)
├── main.py             # Script principal
└── requirements.txt
```

---

## 🛡️ Segurança

> ⚠️ Não compartilhe sua chave da OpenAI!
> Certifique-se de que o `.env` esteja incluído no `.gitignore`.

---

## 💡 Possíveis melhorias

- Interface gráfica
- Exportação para `.txt` ou `.pdf`
- Suporte a múltiplos idiomas com tradução automática

---

## 🧑‍💻 Autor

Pedro – [GitHub](https://github.com/pplucena03)
