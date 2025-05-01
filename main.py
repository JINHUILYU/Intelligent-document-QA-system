from fastapi import FastAPI
from pydantic import BaseModel
from llm_client import ask_with_context
from rag import retrieve_context
from redis_cache import check_cache, cache_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 添加这一段
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有前端访问，生产中可改成指定域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    query_text: str

@app.post("/ask")
async def ask(query: Query):
    cached = check_cache(query.query_text)
    if cached:
        return {"answer": cached}

    context = retrieve_context(query.query_text)
    answer = ask_with_context(query.query_text, context)
    cache_answer(query.query_text, answer)
    return {"answer": answer}
