import pymysql

def get_db_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",       # MySQL 사용자 이름
        password="root",   # MySQL 비밀번호 (Mobius 설정에 맞게)
        database="mobiusdb",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

