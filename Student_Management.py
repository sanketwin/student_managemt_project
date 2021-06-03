print("-------------------------------------")
print("Welcome to Student Management System")
print("-------------------------------------")
student_Data = {}
def delete_Student():
    if len(student_Data.keys()) != 0:
        roll_Number = int(input("Enter Roll Number :"))
        for key in student_Data.keys(): 
            if key == roll_Number:
                print("Roll Number",key,"Record deleted successfully..!!")
                del student_Data[key]    
                break
            else:
                print("No data available for this Roll Number..!!")
    else:
        print("----- No records to Delete -----")
def update_Student():
    roll_Number = int(input("Enter Roll Number :"))
    for key,values in student_Data.items():
        if roll_Number == key:
            name = input("Enter Name :")
            age = int(input("Enter Age :"))
            email = input("Enter Email :")
            phone = int(input("Enter Phone :"))
            values[0] = name
            values[1] = age
            values[2] = email
            values[3] = phone
            student_Data[key] = [name,age,email,phone]
def search_Student():
    if len(student_Data.keys()) != 0:
        print("----- Search Student -----")
        roll_Number = int(input("Enter Roll Number :"))
        for key,values in student_Data.items():
            if roll_Number == key:
                print("\nName  :{0}\nAge   :{1}\nEmail :{2}\nPhone :{3}".format(values[0],values[1],values[2],values[3]))
            else:
                print("No data available for this Roll Number..!!")
    else:
        print("----- No records to Search -----")
def view_Student():
    if len(student_Data.keys()) != 0:
        print("--- Student Records ---")
        print("Roll Number\t","Name\t\t","Age\t","Email\t\t\t","Phone")
        print("---------------------------------------------------------------------------")
        for key,values in student_Data.items():
            print("{0:>5}{1:>25}{2:>6}{3:>25}{4:>15}".format(key,values[0],values[1],values[2],values[3]))
    else:
        print("----- No records to show -----")    
def add_Student():
    roll_Number = int(input("Enter Roll Number :"))
    if len(student_Data.keys()) == 0:
        name = input("Enter Name :")
        age = int(input("Enter Age :"))
        email = input("Enter Email :")
        phone = int(input("Enter Phone :"))
        student_Data[roll_Number] = [name,age,email,phone]
        print(student_Data)
    elif len(student_Data.keys()) != 0 :
            for key in student_Data.keys():
                if key == roll_Number:
                    print("Record for this Roll Number is already available..!!")
    main_System()
def main_System():
    while True:
        print("\n1.Add New Student\n2.View Students\n3.Search Student\n4.Update Student\n5.Delete Student\n6.Quit\n")
        choice = int(input("Enter Your Choice :"))
        if choice == 1:
            add_Student()
            break
        elif choice == 2:
            view_Student()
        elif choice == 3:
            search_Student()
        elif choice == 4:
            update_Student()
        elif choice == 5:
            delete_Student()
        elif choice == 6:
            print("\n-------------------------------------")
            print("Thank you for using our system")
            print("-------------------------------------\n")
            exit()
        else:
            print("Please choose correct option..!!!")
main_System()