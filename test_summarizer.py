from utils.summarizer import summarize_text

# Load transcript from file
with open("sample_transcript.txt", "r", encoding="utf-8") as f:
    transcript = f.read()

# Run summarizer
overview, keypoints, topics = summarize_text(transcript)

# Print results
print("\n=== 📘 OVERVIEW ===")
print(overview)

print("\n=== 🔑 KEYPOINTS ===")
print(keypoints)

print("\n=== 📌 TOPICS ===")
print(", ".join(topics))
