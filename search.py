import numpy as np
from couchbase_setup import get_couchbase_cluster
from embeddings import generate_embedding

collection = get_couchbase_cluster()

# Find the most similar document
def search_similar(query):
    query_embedding = generate_embedding(query)
    
    docs = collection.get("doc1").content_as[dict]
    stored_embedding = np.array(docs["embedding"])
    
    # Compute cosine similarity
    similarity = np.dot(query_embedding, stored_embedding) / (np.linalg.norm(query_embedding) * np.linalg.norm(stored_embedding))
    
    print(f"🔍 Similarity Score: {similarity}")
    if similarity > 0.8:
        print(f"✅ Most relevant document: {docs['text']}")
    else:
        print("❌ No relevant document found.")

# Run search
search_query = "What is Couchbase?"
search_similar(search_query)