import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer from local folder
MODEL_PATH = "falcon-7b"

print("⏳ Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype="auto", device_map="auto")

# Function to generate AI responses
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")  # Ensure it runs on GPU
    with torch.no_grad():
        output = model.generate(**inputs, max_length=100)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Test the model
user_input = input("Ask something: ")
response = generate_response(user_input)
print("🤖 AI Response:", response)
