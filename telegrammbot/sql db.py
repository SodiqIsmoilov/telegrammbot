import sqlite3

db = sqlite3.connect('bot.db')
sql = db.cursor()

sql.execute(""""CREATE TABLE IF NOT EXISTS users(
test_num INT,
answer TEXT
)""")
db.commit()

user_test_num = input('Test nomer: ')
user_test_answer = input('Test javobi: ')

sql.execute("SELECT test_num FROM users")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO users VALUES('{user_test_num}','{user_test_answer}')")
    db.commit()
else:
    print('Bunday nomerdagi test mavjud !!!')
    for value in sql.execute("SELECT * FROM users"):
        print(value)
