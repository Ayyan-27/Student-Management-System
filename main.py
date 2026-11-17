import json

try:


    with open("students.json","r") as f:
        data = json.load(f)

except FileNotFoundError:
    data = {
    "student" : []
    }

def add_students():
    roll_no = int(input("enter your roll_no : "))
    for i in data["student"]:
        if i["roll_no"] == roll_no:
            print("student already exist")
            return

    name = input("enter your name : ")
    father_name = input("enter your father name :")
    your_class = input("enter your class : ")
    phone_num = input("enter your phone number : ")

    student = {
        "roll_no" : roll_no,
        "name" :name,
        "father_name" : father_name,
        "your_class" : your_class,
        "phone_num" : phone_num
    }

    data["student"].append(student)
    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)

def search_student():
    if not data["student"]:
        print("no student found")
    else:
        search_stud = int(input("enter your roll number : "))
        for i in data["student"]:
            if search_stud == i["roll_no"]:
                print(i)
                break
        else:
            print("student not exist")

def update_student():

    print("for update roll number press: 1\n for update phone number press: 2")
    update_choice = int(input("which one you update, roll number or phone number :- "))
    search_roll_no = int(input("enter student roll number :- "))
    for i in data["student"]:
        if search_roll_no == i["roll_no"]: 
            print(i)
            if update_choice == 1:
                new_roll_no = int(input("enter your new roll number:- "))
                for s in data["student"]:
                    if new_roll_no == s["roll_no"] and s["roll_no"] != search_roll_no:
                        print("roll number already exist")
                        break
                else:
                    i["roll_no"] = new_roll_no
            elif update_choice == 2:
                new_phone_no = input("enter your new phone number:- ")
                i["phone_num"] = new_phone_no
            break
    else:
        print("student not found")

    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)

def delete_student():
    delete_roll_no = int(input("enter student roll number:- "))
    for i in data["student"]:
        if delete_roll_no == i["roll_no"]:
            print("Are you sure you want to delete this student.")
            check_value = input("yes or no:- ")
            if check_value == "yes":
                print("student delete")
                data["student"].remove(i)
                break
            
            else:
                print("deletion canceled")
                break

    else:
       print("student not found")

    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)

def view_students():
    if not data["student"]:
        print("students data not found.")
    else:
        print(f"{'roll_no':<10}{'name':<15}{'class':<12}{'father_name':<15}{'phone_number':<15}")
        for i in data["student"]:
            print(f"{i['roll_no']:<10}{i['name']:<15}{i['your_class']:<12}{i['father_name']:<15}{i['phone_num']:<15}")


def exit_program():
    exit()

while True:

    print("1 for add student")
    print("2 for search student details")
    print("3 for update student details")
    print("4 for delete student")
    print("5 for view all students detail")
    print("6 for exit")

    choice = int(input("enter your choice :- "))

    if choice == 1:
        add_students()

    elif choice == 2:
        search_student()

    elif choice == 3:
        update_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        view_students()

    elif choice == 6:
        exit_program()

    else:
        print("Invalid choice! Please try again.")