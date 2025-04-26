from transformers import AutoModelForCausalLM, AutoTokenizer

# Model name
MODEL_NAME = "tiiuae/falcon-7b-instruct"

# Load model and tokenizer
print("⏳ Downloading model, please wait...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype="auto", device_map="auto")

# Save model locally
model.save_pretrained("./falcon-7b")
tokenizer.save_pretrained("./falcon-7b")

print("✅ Model downloaded and saved in 'falcon-7b/' folder!")
