from transformers import pipeline
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

# ---------------------------------------------------
# Ensure required NLTK resources are downloaded
# ---------------------------------------------------
nltk_packages = [
    "punkt",                       # sentence tokenizer
    "punkt_tab",                   # tokenizer tables
    "averaged_perceptron_tagger",  # POS tagging
    "averaged_perceptron_tagger_eng", # some versions require this
    "wordnet",                     # WordNet dictionary
    "omw-1.4"                      # Open Multilingual Wordnet (needed by wordnet)
]

for pkg in nltk_packages:
    try:
        nltk.data.find(pkg)
    except LookupError:
        nltk.download(pkg)

# ---------------------------------------------------
# Load models
# ---------------------------------------------------
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Use sklearn stopwords (more reliable than nltk stopwords)
STOPWORDS = ENGLISH_STOP_WORDS

# ---------------------------------------------------
# Helper functions
# ---------------------------------------------------
def chunk_text(text, max_tokens=800):
    """Split transcript into smaller chunks to fit model limits."""
    sentences = sent_tokenize(text)
    chunks, current_chunk, current_len = [], [], 0

    for sent in sentences:
        tokens = sent.split()
        if current_len + len(tokens) > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk, current_len = [], 0
        current_chunk.append(sent)
        current_len += len(tokens)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


def summarize_text(text, length="short"):
    # Step 1: Split into chunks
    chunks = chunk_text(text)

    # Step 2: Summarize each chunk
    partial_summaries = []
    for chunk in chunks:
        summary = summarizer(
            chunk,
            max_length=150,
            min_length=50,
            do_sample=False
        )[0]["summary_text"]
        partial_summaries.append(summary)

    # Step 3: Merge summaries
    merged_summary = " ".join(partial_summaries)

    # Step 4: Split into sentences
    sentences = sent_tokenize(merged_summary)

    # Step 5: Overview = first 1–2 sentences
    overview = " ".join(sentences[:2])

    # Step 6: Bullet keypoints
    bullets = ["- " + s.strip() for s in sentences]
    keypoints = "\n".join(bullets)

    # Step 7: Extract topics
    words = word_tokenize(merged_summary.lower())
    words = [w for w in words if w.isalpha() and w not in STOPWORDS]
    common = [w for w, _ in Counter(words).most_common(6)]

    return overview, keypoints, common
