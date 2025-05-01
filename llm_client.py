from openai import OpenAI
from openai.types.chat import (
    ChatCompletionUserMessageParam,
    ChatCompletionSystemMessageParam
)
import os
from dotenv import load_dotenv
from pathlib import Path
from typing import Union, List

# 定义合法的消息类型
MessageType = Union[
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam
]

# 自动定位 .env 文件路径
BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

# 加载环境变量
try:
    if not load_dotenv(ENV_PATH):
        raise FileNotFoundError("未找到 .env 文件")
except Exception as e:
    print(f"配置加载失败: {e}")
    exit(1)

# 初始化客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_API_URL")
)

def ask_with_context(query: str, context: str) -> str:
    # 使用类型化字典构造消息
    messages: List[MessageType] = [
        ChatCompletionSystemMessageParam(
            role="system",
            content="基于以下上下文回答问题，如果不知道就说不知道"
        ),
        ChatCompletionUserMessageParam(
            role="user",
            content=f"Context: {context}\nQuestion: {query}"
        )
    ]
    print(f"query: {query}")
    print(f"context: {context}")

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,  # 现在类型校验可以通过
            max_tokens=200,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as err:
        print(f"API请求失败: {err}")
        return "暂时无法回答"

if __name__ == "__main__":
    test_query = "What is the capital of France?"
    test_context = "The capital of France is Paris."
    answer = ask_with_context(test_query, test_context)
    print(f"Answer: {answer}")