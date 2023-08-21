from datetime import datetime
#https://stackoverflow.com/questions/61097144/reading-operations-line-by-line-and-making-eval-for-each-line
#https://www.freecodecamp.org/news/python-import-from-file-importing-local-files-in-python/
#The Big O notation for the given load_employee_data() function is O(n) depending on employees.txt
def load_employee_data():
    employees = {}
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                emp_id, username, timestamp, gender, salary = line.strip().split(", ")
                employees[emp_id] = {"username": username,"emp_id": emp_id,"timestamp": timestamp,"gender": gender,"salary": float(salary)}
        print("Employee data loaded successfully.")
    except FileNotFoundError:
        print("No employee data found.")
    except Exception as e:
        print("Error loading employee data:", e)
    return employees

#O(n) or O(1)
def admin_menu():
    employees = load_employee_data()
    while True:
        print("Admin Menu")
        print("1 To Display Statistics")
        print("2 To Add an Employee")
        print("3 To Display all Employees")
        print("4 To Change Employee’s Salary")
        print("5 To Remove Employee")
        print("6 To Raise Employee’s Salary")
        print("7 To Exit and Save")

        choose = input("Enter task number: ")

        if choose == "1":
            Display_Statistics(employees)
        elif choose == "2":
            Add_Employee(employees)
        elif choose == "3":
            display_all_employees(employees)
        elif choose == "4":
            Change_Salary(employees)
        elif choose == "5":
            Remove_Employee(employees)
        elif choose == "6":
            Raise_Salary(employees)
        elif choose == "7":
            save_exit(employees)
            print("Exiting the program.")
            break
        else:
            print("Invalid task number. Please choose again.")

#O(n), where n is the number of employees.
def Display_Statistics(employees):
    male = 0
    female = 0
  #https://www.geeksforgeeks.org/python-dictionary-values/
    for emp in employees.values():
        if emp["gender"] == "male":
            male =male+1
        elif emp["gender"] == "female":
            female =female+1
    
    print("Number of male employees: ",male)
    print("Number of female employees: ",female)
  
#O(1)
def Add_Employee(employees):
  #to add new employee just add username,gender,and salary
    emp_id = f"emp{len(employees) + 1:03}"
    username = input("Enter new employee's username: ")
    gender = input("Enter employee's gender: ")
    salary = int(input("Enter employee's salary: "))
  #https://www.tutorialspoint.com/how-to-add-timestamp-to-excel-file-in-python
    timestamp = datetime.today().strftime("%Y%m%d")
  #id is incremented and the time is automatic
    
    employees[emp_id] = {"username": username,"emp_id": emp_id,
"timestamp": timestamp,"gender": gender,"salary": salary}
    
    print("Employee added successfully.")
#O(n log n) due to the sorting operation.
def display_all_employees(employees):
  #display all the employees registered in the system ordered by date
  #https://realpython.com/python-sort/
    sorted_employees = sorted(employees.values(), key=lambda emp: emp["timestamp"], reverse=True)
    for emp in sorted_employees:
        print(f"Employee ID: {emp['emp_id']}")
        print(f"Username: {emp['username']}")
        print(f"Timestamp: {emp['timestamp']}")
        print(f"Gender: {emp['gender']}")
        print(f"Salary: {emp['salary']}")
        print()

# O(1)
def Change_Salary(employees):
    emp_id = input("Enter the Employee ID whose salary you want to change: ")
    new_salary = int(input("Enter the new salary: "))

    if emp_id in employees:
        employees[emp_id]["salary"] = new_salary
        print("Salary changed successfully.")
    else:
        print("Employee not found.")

#O(1)
def Remove_Employee(employees):
    emp_id = input("Enter the Employee ID of the employee you want to remove: ")

    if emp_id in employees:
        del employees[emp_id]
        print("Employee removed successfully.")
    else:
        print("Employee not found.")

#O(1)
def Raise_Salary(employees):
    emp_id = input("Enter the Employee ID of the employee whose salary you want to raise: ")
    raise_percentage = float(input("Enter the raise percentage: "))

    if emp_id in employees:
        employees[emp_id]["salary"] =  employees[emp_id]["salary"]*raise_percentage+ employees[emp_id]["salary"]
        print("Salary raised successfully.")
    else:
        print("Employee not found.")

#O(n), where n is the number of employees
#https://realpython.com/python-csv/
def save_exit(employees):
    try:
        with open("employees.txt", "w") as file:
            for emp_id, emp_info in employees.items():
                line = f"{emp_info['emp_id']}, {emp_id}, {emp_info['timestamp']}, {emp_info['gender']}, {emp_info['salary']}\n"
                file.write(line)
        print("Employee data saved successfully.")
    except Exception as e:
        print("Error saving employee data:", e)

#O(1)
#to check if working enter the emp id not the username
def user_menu(username, employees):
    while True:
        print("\nUser Menu")
        print("1 to Check my salary")
        print("2 to Exit")

        choose = input("Enter your task number: ")  # choose whatever task they wanna make

        if choose == "1":
            check_my_salary(username, employees)
        elif choose == "2":
            exit_timestamp(username, employees)
            break
#O(1)
def check_my_salary(username, employees):
    if username in employees:
        salary = employees[username]["salary"]
        print("Your salary is:", salary)
    else:
        print("Username not found.")

#O(1)
def exit_timestamp(username, employees):
    timestamp = datetime.now().strftime("%Y-%m-%d %a %H:%M:%S")
    with open("user_login.txt", "a") as file:
        file.write(f"{username},{timestamp}\n")
    if username in employees:
        employees[username]["last_exit"] = timestamp
        print("Exit timestamp recorded.")
    else:
        print("Username not found.")
#O(n + m), where n is the number of attempts allowed in the loop and m is the number of employees,and m is the number of employees
def login_form():
    attempts = 0
    employees = load_employee_data()
    usernames = [emp["username"] for emp in employees.values()]
    while attempts < 5:
        username = input("Username: ")

        if username == "admin":
            password = input("Password: ")
            if password == "admin123123":
                print("Successfully logged in to Admin's Menu")
                admin_menu()
                break
            else:
                print("Invalid password.")
        elif username in usernames:
            print("Successfully logged in to User's Menu")
            gender = employees[username]['gender']
            salutation = 'Mr.' if gender == 'male' else 'Mrs.'
            print("\nHi", salutation, username + "!")
            user_menu(username, employees)
            break
        else:
            print("Invalid username.")
            attempts += 1

    if attempts >= 5:
        print("Maximum login attempts exceeded.")

login_form()