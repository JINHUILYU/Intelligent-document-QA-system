from sentence_transformers import SentenceTransformer
import numpy as np
import pickle
from db import get_db_connection
from redis_client import get_redis_client

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
r = get_redis_client()

def save_embeddings_to_redis():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM documents")
    documents = cursor.fetchall()

    for doc_id, content in documents:
        embedding = model.encode(content)
        redis_key = f"doc:{doc_id}"
        r.hset(redis_key, mapping={
            "content": content,
            "embedding": pickle.dumps(embedding)
        })

    print("✅ All embeddings saved to Redis")

if __name__ == "__main__":
    save_embeddings_to_redis()
