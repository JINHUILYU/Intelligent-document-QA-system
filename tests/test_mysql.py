# 测试 mysql
import mysql.connector
import os
import sys



def test_mysql_connection():
    # 配置连接参数（根据实际情况修改）
    mysql_config = {
        "host": "localhost",
        "user": "root",
        "password": "123456",
        "database": "document_qa",
        "raise_on_warnings": True,
        "use_pure": True,
        "connection_timeout": 5
    }

    try:
        # 创建连接
        conn = mysql.connector.connect(**mysql_config)

        # 测试连接是否成功
        if conn.is_connected():
            print("✅ MySQL 连接成功")

        # 测试数据读写
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()[0]
        print(f"🔑 当前数据库: {db_name}")

        # 清理测试数据
        cursor.close()
        conn.close()

        return True
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("🔒 认证失败: 请检查用户名和密码")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("❌ 数据库不存在")
        else:
            print(f"❌ 连接失败: {err}")
    except Exception as e:
        print(f"❌ 未知错误: {e}")
    return False

if __name__ == "__main__":
    test_mysql_connection()