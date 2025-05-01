from redis_client import get_redis_client
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
r = get_redis_client()


def retrieve_context(query: str, top_k=3) -> str:
    query_vec = model.encode(query)

    # 扫描所有文档 key
    doc_keys = r.keys("doc:*")
    contents = []
    embeddings = []

    for key in doc_keys:
        content = r.hget(key, "content").decode("utf-8")
        embedding = pickle.loads(r.hget(key, "embedding"))
        contents.append(content)
        embeddings.append(embedding)

    embeddings = np.array(embeddings)
    sims = cosine_similarity([query_vec], embeddings)[0]
    top_indices = sims.argsort()[-top_k:][::-1]

    return " ".join([contents[i] for i in top_indices])
