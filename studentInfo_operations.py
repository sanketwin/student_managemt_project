from db import conn,cur

def add_Student():
    roll_no = int(input("Enter roll number :"))
    name = input("Enter Name :")
    age = int(input("Enter Age :"))
    email = input("Enter Email :")
    phone = int(input("Enter Phone :"))

    cur.execute("insert into student_management values (%s,%s,%s,%s,%s)",(roll_no,name,age,email,phone))
    conn.commit()
    print("Record Added Successfully...!!")

def view_Student():
    cur.execute("select * from student_management")
    data = cur.fetchall()
    for rows in data:
        print("Roll Number")


def search_Student():
    roll_no = int(input("Enter roll number :"))
    cur.execute("select * from student_management where roll_no=%s",(roll_no))
    data =cur.fetchone()
    print("\nName  :{0}\nAge   :{1}\nEmail :{2}\nPhone :{3}".format(data[1],data[2],data[3],data[4]))

def update_Student():
    roll_no = int(input("Enter roll number :"))
    cur.execute("select * from student_management where roll_no=%s",(roll_no))
    data =cur.fetchone()
    if roll_no == data[0]:
        name = input("Enter Name :")
        age = int(input("Enter Age :"))
        email = input("Enter Email :")
        phone = int(input("Enter Phone :"))
        cur.execute("update student_management set name=%s,age=%s,email=%s,contact=%s where roll_no=%s",(name,age,email,phone,roll_no))
        conn.commit()
def delete_Student():
    roll_no = int(input("Enter roll number :"))
    cur.execute("delete from student_management where roll_no=%s",(roll_no))
    conn.commit()