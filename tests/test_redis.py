import redis

def test_redis_connection():
    # 配置连接参数（根据实际情况修改）
    redis_config = {
        "host": "localhost",
        "port": 6379,
        "password": None,  # 如果有密码需要填写
        "db": 0,
        "socket_timeout": 5
    }

    try:
        # 创建连接池
        pool = redis.ConnectionPool(**redis_config)
        r = redis.Redis(connection_pool=pool)

        # 测试 PING 命令
        if r.ping():
            print("✅ Redis 连接成功")

        # 测试数据读写
        test_key = "test_key"
        r.set(test_key, "hello redis")
        value = r.get(test_key)
        print(f"🔑 测试键值读取: {value.decode()}")

        # 清理测试数据
        r.delete(test_key)

        return True
    except redis.AuthenticationError as e:
        print(f"🔒 认证失败: {e}")
    except redis.ConnectionError as e:
        print(f"🔌 连接失败: 请检查 Redis 服务是否运行在 {redis_config['host']}:{redis_config['port']}")
    except Exception as e:
        print(f"❌ 未知错误: {e}")
    return False


if __name__ == "__main__":
    test_redis_connection()