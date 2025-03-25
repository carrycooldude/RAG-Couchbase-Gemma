# 🧠 RAG System using Couchbase and Gemma 3

## 🚀 Overview  
This project implements a **Retrieval-Augmented Generation (RAG)** system using:  
- **Gemma 3** for text embedding & generation.  
- **Couchbase** as the vector database to store & retrieve embeddings.  
- **Python** for the full pipeline.  

## 📦 Setup  

### 1️⃣ Install Dependencies  
First, create a **virtual environment** and install required libraries:  
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ Install & Setup Couchbase  
**Option 1: Using Docker (Recommended)**  
```bash
docker run -d --name couchbase -p 8091-8096:8091-8096 -p 11210:11210 couchbase
```
Then, open `http://localhost:8091` in your browser to complete setup.  

**Option 2: Manual Installation**  
Download Couchbase from [official site](https://www.couchbase.com/downloads) and install it manually.

### 3️⃣ Setup Couchbase Buckets & Indexes  
Run the setup script to create a bucket and indexes:  
```bash
python couchbase_setup.py
```

---

## 🔧 How to Use  

### 1️⃣ Generate & Store Embeddings  
Run `embeddings.py` to process documents and store their embeddings in Couchbase:  
```bash
python embeddings.py
```

### 2️⃣ Query Using RAG Pipeline  
Retrieve relevant information using a query:  
```bash
python query.py "Your search query here"
```

---

## 📝 Example Usage  

#### **1️⃣ Store a Document**  
```python
store_embedding("doc1", "This is an example document about AI and machine learning.")
```

#### **2️⃣ Query the Database**  
```python
results = retrieve_relevant_docs("Tell me about AI")
```

#### **3️⃣ Generate an Answer**  
```python
response = generate_answer("Tell me about AI", results)
print(response)
```

---

## 🔗 References  
- [Couchbase Docs](https://docs.couchbase.com/home/index.html)  
- [Gemma 3 by Google](https://ai.google.dev/models/gemma)