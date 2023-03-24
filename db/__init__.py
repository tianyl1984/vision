import sqlite3

conn = sqlite3.connect('vision.db')
cursor = conn.cursor()

# 从 SQL 文件中读取 SQL 语句
with open('db/init.sql', 'r', encoding='utf-8') as f:
    sql = f.read()

# 根据分号拆分 SQL 语句
statements = sql.split(';')

# 执行每个 SQL 语句
for statement in statements:
    cursor.execute(statement)

# 提交修改
conn.commit()

# 关闭连接
conn.close()

print("数据库初始化完成")
