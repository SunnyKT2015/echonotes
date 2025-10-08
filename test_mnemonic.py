from utils.mnemonic import generate_mnemonic

topics = ["Data", "Analysis", "Security", "Health", "Education"]

result = generate_mnemonic(topics)

print("📋 Topics:", topics)
print("🔑 Acronym:", result["acronym"])
print("💡 Phrase:", result["phrase"])
