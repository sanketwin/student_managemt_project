import studentInfo_operations as info

def main():
    while True:
        print("\n1.Add New Student\n2.View Students\n3.Search Student\n4.Update Student\n5.Delete Student\n6.Quit\n")
        choice = int(input("Enter Your Choice :"))
        if choice == 1:
            info.add_Student()
        elif choice == 2:
            info.view_Student()
        elif choice == 3:
            info.search_Student()
        elif choice == 4:
            info.update_Student()
        elif choice == 5:
            info.delete_Student()
        elif choice == 6:
            exit()
main()