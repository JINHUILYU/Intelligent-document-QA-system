import redis

# 当前知识库的版本号（知识更新时修改）
KNOWLEDGE_VERSION = "v1"

# Redis 配置
r = redis.Redis(host='localhost', port=6379, db=0)

def make_cache_key(query: str) -> str:
    return f"{KNOWLEDGE_VERSION}:{query.strip()}"  # 避免前后空格影响 key

def check_cache(query: str) -> str | None:
    key = make_cache_key(query)
    result = r.get(key)
    return result.decode('utf-8') if result else None

def cache_answer(query: str, answer: str, ttl: int = 3600) -> None:
    key = make_cache_key(query)
    r.setex(key, ttl, answer)

def clear_all_cache() -> None:
    """⚠️ 清除 Redis 中所有键值（整个 DB）"""
    r.flushdb()

def clear_cache_by_version(version: str = KNOWLEDGE_VERSION) -> None:
    """根据版本清理旧缓存（保留其他版本的）"""
    pattern = f"{version}:*"
    for key in r.scan_iter(pattern):
        r.delete(key)

def get_all_keys() -> list[str]:
    """调试用，列出所有缓存键"""
    return [key.decode("utf-8") for key in r.scan_iter("*")]

def get_cached_value(key: str) -> str | None:
    result = r.get(key)
    return result.decode("utf-8") if result else None
