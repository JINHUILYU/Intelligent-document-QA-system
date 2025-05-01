# 📘 LLM-powered 智能文档问答系统

基于 RAG（Retrieval-Augmented Generation）的智能问答系统，支持文档知识库构建、语义检索与大语言模型（LLM）问答，通过 Redis 提高响应速度，并支持 MySQL 持久化存储。

---

## 🔧 技术栈

- **Python**
- **FastAPI** - 构建高性能 Web API
- **MySQL** - 存储文档内容
- **Redis** - 缓存问答结果
- **RAG** - 检索增强生成策略
- **大型语言模型 API**（如 OpenAI 或本地 LLM）
- 可选：**Docker / Kubernetes** - 容器化部署与扩展

---

## 📁 项目结构

```
├── main.py # 启动入口
├── rag.py # 语义检索 + 文档生成逻辑
├── redis_cache.py # Redis 缓存工具
├── db.py # 数据库连接工具
├── insert_documents.py # 插入知识库内容 
├── requirements.txt 
├── README.md 
├── .gitignore
├── tests/ # 测试程序目录
│ ├── test_redis.py # 测试 Redis
│ └── test_mysql.py # 测试 MySQL
└── .env # 存储数据库 / API 密钥配置（可选）
```

---

## 🚀 快速开始

### 1. 克隆项目

```bash
  git clone
```

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

> 你需要确保本地已安装并启动 **MySQL** 和 **Redis**。

### 2. 初始化数据库

```sql
-- 使用你的 MySQL 客户端执行以下命令：

CREATE DATABASE IF NOT EXISTS document_qa;
USE document_qa;

CREATE TABLE documents (
  id INT AUTO_INCREMENT PRIMARY KEY,
  content TEXT
);
```

### 3. 插入测试文档

```bash
python app/insert_documents.py
```

### 4. 启动服务

```bash
uvicorn app.main:app --reload
```

---

## ✨ 示例 API

### 文档问答接口（POST）

```
POST /ask
```

#### 请求参数：

```json
{
  "query": "什么是 Redis？"
}
```

#### 返回结果：

```json
{
  "answer": "Redis 是一个基于内存的键值数据库...",
  "source_documents": ["Redis 是一个基于内存的键值数据库..."]
}
```

---

## ⚙️ 缓存说明（Redis）

- 每次查询会先检查 Redis 中是否已有结果。
- 若未命中缓存，则通过 RAG 进行语义检索并调用大语言模型生成回答，并将结果缓存 1 小时。
- 支持知识库版本控制，更新文档后自动清理旧缓存。

---

## 📖 RAG 原理

本项目使用简化版 RAG：

1. 将问题与所有文档语义对比，取相似度最高的内容。
2. 拼接为上下文传给语言模型生成答案。
3. 使用 Redis 加速相同问题的重复查询。

> 后续可接入向量数据库如 FAISS、Chroma 提升检索效率。

---

## 📝 License

本项目仅供学习和研究使用，未授权商用。