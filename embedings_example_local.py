import torch
from sentence_transformers import SentenceTransformer

# Check if Apple Silicon GPU is available
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device}")

# Load the model onto the GPU
model = SentenceTransformer('all-MiniLM-L6-v2', device=device)

text = "1"
embedding = model.encode(text)
print(f"Embedding for '{text}': {embedding}")

print("Success!")
