import nltk

# List of all required resources
resources = [
    "punkt",
    "punkt_tab",
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng",
    "stopwords"
]

for r in resources:
    try:
        nltk.download(r)
        print(f"✅ Downloaded: {r}")
    except Exception as e:
        print(f"❌ Failed to download {r}: {e}")

print("🎉 All NLTK resources downloaded successfully!")
