import os
from couchbase_setup import get_couchbase_cluster

collection = get_couchbase_cluster()

# Store a text document in Couchbase
def store_document(doc_id, text):
    collection.upsert(doc_id, {"text": text})
    print(f"✅ Stored document: {doc_id}")

# Read and store document
with open("data/sample.txt", "r") as file:
    text = file.read()
    store_document("doc1", text)