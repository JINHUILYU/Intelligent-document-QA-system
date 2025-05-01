from db import get_db_connection


def insert_sample_documents():
    docs = [
        "Python 是一种解释型、动态类型的编程语言，具有良好的可读性。",
        "Redis 是一个基于内存的键值数据库，常用于缓存和实时分析场景。",
        "Docker 是一个容器化平台，用于打包和部署应用。",
        "Kubernetes 是一个用于容器编排的开源系统。",
        "FastAPI 是一个用于构建高性能 API 的现代 Web 框架。",
        "向量数据库可以用来存储嵌入向量，并用于语义检索。",
        "机器学习是一种通过数据训练模型的方法，用于进行预测和分类。",
        "大语言模型可以用来实现智能问答、文本生成等功能。",
        "MySQL 是一个流行的关系型数据库，支持 SQL 语言。",
        "RAG（检索增强生成）结合了文档检索和语言模型生成的能力。"
    ]

    conn = get_db_connection()
    cursor = conn.cursor()

    for doc in docs:
        cursor.execute("INSERT INTO documents (content) VALUES (%s)", (doc,))

    conn.commit()
    conn.close()
    print("✅ 测试文档已成功插入数据库")


if __name__ == "__main__":
    insert_sample_documents()
