import numpy as np
from couchbase_setup import get_couchbase_cluster
import google.generativeai as genai

# Set up the API key
genai.configure(api_key="YOUR_API_KEY")

# Generate embedding using Google's embedding model
def generate_embedding(text):
    embedding = genai.embed_content(
        model='models/embedding-001',
        content=text,
        task_type="retrieval_document"
    )
    return np.array(embedding['embedding'])

# Rest of your code...

# Store embedding in Couchbase
def store_embedding(doc_id, text):
    collection = get_couchbase_cluster()
    if not collection:
        print("❌ Couchbase connection failed")
        return

    embedding = generate_embedding(text)
    document = {"text": text, "embedding": embedding.tolist()}
    collection.upsert(doc_id, document)
    print(f"✅ Stored embedding for document ID: {doc_id}")

if __name__ == "__main__":
    doc = {"text": "Couchbase is a high-performance NoSQL database."}
    store_embedding("doc1", doc["text"])