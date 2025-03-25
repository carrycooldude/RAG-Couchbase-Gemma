from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load Gemma 3
model_name = "google/gemma-3b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# Generate AI response
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_length=200)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Example usage
query = "Tell me about Couchbase."
print("🤖 AI Response:", generate_response(query))