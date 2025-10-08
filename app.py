import streamlit as st
from pathlib import Path
import whisper

# ----------------------------
# 🔹 Page Setup (must be first!)
# ----------------------------
st.set_page_config(
    page_title="🎙️ EchoNotes",
    page_icon="🎧",
    layout="wide",
)


# ----------------------------
# 🔹 Custom CSS for Better UI
# ----------------------------
st.markdown("""
<style>
/* ---------- General Page Styles ---------- */
body {
  font-family: "Segoe UI", sans-serif;
  background-color: #fafafa;
}

/* ---------- Header ---------- */
.app-header {
  text-align: center;
  padding: 20px 0 10px 0;
}
.app-title {
  color: #1E40AF;
  font-size: 48px;
  margin: 0;
  font-weight: 700;
}
.app-sub {
  color: #6B7280;
  font-size: 16px;
  margin-top: 6px;
  margin-bottom: 8px;
}
hr {
  border: 1px solid #e5e7eb;
  width: 90%;
}

/* ---------- Section Layout ---------- */
.section {
  background: #ffffff;
  border-radius: 10px;
  padding: 20px 25px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  margin-bottom: 25px;
}

/* ---------- Buttons ---------- */
div.stButton > button {
  background-color: #2563EB;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}
div.stButton > button:hover {
  background-color: #1D4ED8;
  transform: translateY(-1px);
}

/* ---------- Inline Button Header ---------- */
.header-with-button {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 10px;
}
.header-with-button h2 {
  margin: 0;
  font-size: 36px;
  color: #111827;
}

/* ---------- Section Headings ---------- */
h2 {
  color: #111827;
}

/* ---------- Footer ---------- */
.app-footer {
  text-align: center;
  color: #9ca3af;
  margin-top: 25px;
  font-size: 14px;
}

/* ---------- Download Buttons ---------- */
.download-section div.stButton > button {
  width: 100%;
  margin-top: 8px;
}

/* ---------- Text Area ---------- */
textarea {
  border-radius: 8px !important;
  padding: 10px !important;
  font-size: 15px !important;
}
</style>
""", unsafe_allow_html=True)




# ----------------------------
# 🔹 Page Heading
# ----------------------------
st.markdown("""
<div class="app-header">
  <h1 class="app-title">🎙️ EchoNotes</h1>
  <p class="app-sub">Convert lecture audio/video into concise notes, key points and handy mnemonics — download as TXT or PDF.</p>
  <hr style="border:1px solid #e6e9ef; width:90%; margin-top:10px;">
</div>
""", unsafe_allow_html=True)
# ----------------------------
# 🔹 Directories
# ----------------------------
BASE_DIR = Path(__file__).parent
UPLOADS_DIR = BASE_DIR / "uploads"
OUTPUTS_DIR = BASE_DIR / "outputs"
UPLOADS_DIR.mkdir(exist_ok=True)
OUTPUTS_DIR.mkdir(exist_ok=True)


from utils.speech_to_text import transcribe_audio

from utils.summarizer import summarize_text

from utils.mnemonic import generate_mnemonic

from utils.downloads import get_text_file, get_pdf_file

# ----------------------------
# 🔹 Session State
# ----------------------------
if "transcript" not in st.session_state: st.session_state["transcript"] = ""
if "summary" not in st.session_state: st.session_state["summary"] = ""
if "topics" not in st.session_state: st.session_state["topics"] = []
if "mnemonic" not in st.session_state: st.session_state["mnemonic"] = ""

# ----------------------------
# 📂 Upload Section
# ----------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("📂 Upload Lecture")
uploaded = st.file_uploader("Upload audio or video", type=["mp3","wav","m4a","mp4","mov","mkv"])

if uploaded:
    st.success(f"Uploaded: {uploaded.name}")
    st.audio(uploaded)

    if st.button("Generate Transcript"):
        with st.spinner("Transcribing..."):
            transcript = transcribe_audio(uploaded)
            st.session_state["transcript"] = transcript
        st.success("Transcript generated ✅")


    if st.session_state["transcript"]:
        with st.expander("📜 Full Transcript", expanded=False):
            st.text_area("Transcript", st.session_state["transcript"], height=300, label_visibility="collapsed")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")  # divider

# ----------------------------
# 📝 Summary Section
# ----------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="header-with-button"><h2>📝 Summary</h2></div>', unsafe_allow_html=True)

# Generate summary when button clicked
if st.button("Summarize Notes", key="summarize_btn"):
    if "transcript" not in st.session_state or not st.session_state["transcript"]:
        st.warning("Please upload and transcribe first.")
    else:
        overview, keypoints, topics = summarize_text(st.session_state["transcript"])
        st.session_state["summary"] = overview
        st.session_state["keypoints"] = keypoints
        st.session_state["topics"] = topics
        st.success("Summary generated ✅")

# --- Always display if available ---
if st.session_state.get("summary"):
    st.subheader("📘 Overview")
    st.markdown(
        f"<p style='line-height:1.6; color:#1f2937;'>{st.session_state['summary']}</p>",
        unsafe_allow_html=True
    )

if st.session_state.get("keypoints"):
    st.subheader("🔑 Key Points")

    keypoints_text = st.session_state["keypoints"]
    lines = [line.strip() for line in keypoints_text.split('\n') if line.strip()]
    if len(lines) <= 1:
        lines = [kp.strip() for kp in keypoints_text.replace("•", "\n").replace("-", "\n").split('\n') if kp.strip()]

    for line in lines:
        st.markdown(f"<p style='margin-left:10px;'>• {line}</p>", unsafe_allow_html=True)


if st.session_state.get("topics"):
    st.subheader("📌 Topics")
    st.write(", ".join(st.session_state["topics"]))

st.markdown('</div>', unsafe_allow_html=True)


st.markdown("---")

# ----------------------------
# 🧠 Mnemonic Section
# ----------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="header-with-button"><h2>🔑 Mnemonic</h2>', unsafe_allow_html=True)

if st.button("Generate Mnemonic", key="mnemonic_btn"):
    if "topics" not in st.session_state or not st.session_state["topics"]:
        st.warning("Please summarize first to generate topics.")
    else:
        mnemonic_data = generate_mnemonic(st.session_state["topics"])
        st.session_state["mnemonic"] = mnemonic_data
        st.success("Mnemonic generated ✅")

    # Display Mnemonic
    if "mnemonic" in st.session_state:
        data = st.session_state["mnemonic"]

        if isinstance(data, dict):
            st.markdown(f"**Acronym:** {data['acronym']}")
            st.markdown(f"**Mnemonic Sentence:** {data['phrase']}")
        else:
            st.markdown(f"**Mnemonic:** {data}")  # fallback if string
st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")


# ----------------------------
# 📥 Download Section
# ----------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="header-with-button"><h2>⬇️ Download Notes</h2>', unsafe_allow_html=True)

if st.session_state.get("transcript") or st.session_state.get("summary"):
    transcript = st.session_state.get("transcript", "")
    summary = st.session_state.get("summary", "")
    topics = st.session_state.get("topics", [])
    mnemonic_data = st.session_state.get("mnemonic", {"phrase": ""})
    if isinstance(mnemonic_data, dict):
        mnemonic = mnemonic_data.get("phrase", "")
    else:
        mnemonic = mnemonic_data  # already a string

    st.markdown('<div class="download-section">', unsafe_allow_html=True)    
    # Transcript download
    st.download_button("📜 Download Transcript", data=transcript.encode("utf-8"),
                       file_name="transcript.txt", mime="text/plain")

    # Notes as TXT
    txt_file = get_text_file(transcript,summary,st.session_state.get("keypoints", ""),topics,mnemonic)
    

    st.download_button("📝 Download Notes (TXT)", data=txt_file,
                       file_name="notes.txt", mime="text/plain")

    # Notes as PDF
    pdf_file = get_pdf_file(transcript,summary,st.session_state.get("keypoints", ""),topics, mnemonic)

    st.download_button("📄 Download Notes (PDF)", data=pdf_file,
                       file_name="notes.pdf", mime="application/pdf")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Generate transcript and summary first to enable downloads.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("### 📖 About EchoNotes")
st.write("""
**EchoNotes** automatically converts recorded lectures into structured notes.

**Features:**
- 🎙 Converts audio/video to transcript using Whisper
- 🧠 Summarizes long lectures into key concepts
- 💡 Generates mnemonic tricks for easy memory
- 📄 Exports notes in TXT and PDF formats

""")
