import pymysql
conn = pymysql.connect(
    host = "localhost",
    user="root",
    password="2311",
    db="aira"
    )

cur = conn.cursor()
cur.execute("create table if not exists student_management(roll_no int(11), name varchar(50), age int(11), email varchar(50), contact varchar(10))")
conn.commit()
