import whisper
import tempfile
import os

def transcribe_audio(file) -> str:
    """
    Transcribes audio/video file into text using Whisper.
    
    Args:
        file: Uploaded file (Streamlit UploadedFile object)

    Returns:
        transcript (str): Full transcribed text
    """
    model = whisper.load_model("small")
    # Save uploaded file to a temp location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name
    result = model.transcribe(tmp_path)
    # Clean up
    os.remove(tmp_path)
    return result["text"]
