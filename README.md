# 🎙️ EchoNotes — Lecture Voice to Notes Generator

**EchoNotes** is an intelligent Streamlit-based web app that converts **lecture audio or video** into structured, easy-to-understand notes.
It automatically generates **summaries, key points, and mnemonic tricks** to make studying effortless and memory-friendly.

---

## 🚀 Features

✅ **Upload Audio or Video Files** — Supports `.mp3`, `.wav`, `.mp4`, `.mkv`, `.m4a`, and `.mov` formats
✅ **Automatic Transcription** — Uses OpenAI Whisper to convert speech to text
✅ **Smart Summarization** — Condenses long lectures into concise overviews and bullet key points
✅ **Mnemonic Generation** — Creates short mnemonic sentences from key topics for easy recall
✅ **Download Options** — Export your notes in `.txt` and `.pdf` formats
✅ **Beautiful, Simple UI** — Clean Streamlit interface with responsive layout

---

## 🧠 Tech Stack

| Component            | Technology Used                        |
| -------------------- | -------------------------------------- |
| Frontend             | Streamlit                              |
| Speech Recognition   | OpenAI Whisper                         |
| Summarization        | Hugging Face Transformers (BART model) |
| NLP Utilities        | NLTK, Scikit-learn                     |
| PDF Generation       | ReportLab                              |
| Video/Audio Handling | MoviePy, FFmpeg                        |
| Language             | Python 3.10+                           |

---

## 🏗️ Project Structure

```
Voice-Notes Project/
│
├── app.py                          # Main Streamlit web app
├── requirements.txt                # Dependencies
├── README.md                       # Project documentation
│
├── utils/
│   ├── __init__.py
│   ├── speech_to_text.py           # Handles audio/video transcription
│   ├── summarizer.py               # Summarization + keypoints extraction
│   ├── mnemonic.py                 # Mnemonic generation logic
│   ├── downloads.py                # TXT and PDF file generation
│
├── uploads/                        # Stores temporary uploaded files
├── outputs/                        # Stores generated outputs
│
├── test_summarizer.py              # Test script for summarizer
├── test_mnemonic.py                # Test script for mnemonic generation
├── nltk_downloader.py              # Downloads all required NLTK data
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/echonotes.git
cd "Voice-Notes Project"
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the NLTK Downloader Once

```bash
python nltk_downloader.py
```

### 5️⃣ Launch the App

```bash
streamlit run app.py
```

Then open your browser at **[http://localhost:8501](http://localhost:8501)**

---

## 🧩 Example Workflow

1️⃣ Upload your **lecture audio or video**
2️⃣ Click **Generate Transcript** to convert speech to text
3️⃣ Click **Summarize Notes** to get concise explanations and key points
4️⃣ Click **Generate Mnemonic** to get easy memory tricks
5️⃣ Download your notes as **TXT or PDF**

---

## 📦 Requirements

Your `requirements.txt` should include:

```
streamlit==1.39.0
torch==2.4.0
transformers==4.44.2
openai-whisper==20231117
nltk==3.9.1
scikit-learn==1.3.2
pandas==2.2.3
numpy==1.26.4
reportlab==4.2.4
moviepy==1.0.3
ffmpeg-python==0.2.0
```

---

## 🌐 Deployment

### Deploy to **Streamlit Cloud**

1. Push your code to a GitHub repository.
2. Visit [https://share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub → Choose your repo → Set `app.py` as entry point.
4. Streamlit will auto-install dependencies and deploy your app.

You’ll get a public URL like:

```
https://your-username-echonotes.streamlit.app
```

---

## 🧾 Future Enhancements

* 🌙 Dark/Light mode toggle
* 🧠 User login system to save notes
* 📚 Support for multi-language transcription
* 🧮 Improved summarization models

---

## 💡 Credits

Built using:

* **OpenAI Whisper** for transcription
* **Hugging Face Transformers** for summarization
* **Streamlit** for the frontend

---

## 👨‍💻 Author

**SUNNY KIRAN TATAPUDI**
📧 [sunnykirantatapudi@gmail.com](mailto:sunnykirantatapudi@gmail.com)
🔗 [LinkedIn](www.linkedin.com/in/sunny-kiran-tatapudi-65bba832a) | [GitHub](https://github.com/SunnyKT2015)

> “Turning words into wisdom — one lecture at a time.” 🎧

---

## 🪪 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and share it for educational or research purposes.
