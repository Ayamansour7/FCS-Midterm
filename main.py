employees ={} #concerning an empty dictionary
#https://stackoverflow.com/questions/61097144/reading-operations-line-by-line-and-making-eval-for-each-line
#https://www.freecodecamp.org/news/python-import-from-file-importing-local-files-in-python/
def load_employees():
    with open("employees.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                employee = eval(line)
                username = employee["username"]
                employees[username] ={"emp_id":emp_id,"timestamp": timestamp,"gender": gender,"salary": int(salary)}

def admin_menu(): #function for user menu
  while True:
    print("\nAdmin Menu")
    print("1 to Display Statistics")
    print("2 to Add an Employee")
    print("3 Display all Employees")
    print("4 to Change Employee’s Salary")
    print("5 to Remove Employees")
    print("6 to Raise Employee’s Salary")
    print("7 to Save and Exit")
  

    choose=input("Enter your task number: ") #choose whatever task they wanna make 

    if choose=="1":
      display_statistics()
    elif choose=="2":
      add_employee()
    elif choose=="3":
      display_all_employees()
    elif choose=="4":
      change_salary()
    elif choose=="5":
      remove_employee()
    elif choose=="6":
      raise_salary()
    elif choose=="7":
      save_exit() #make sure to save all the changed information before exiting 
      break
    else:
      print("Task not valid,Try again") #while entering any value different the ones mentioned



#write the display statistics function to see how many males and females
def display_statistics():
  males=0
  females=0
  for employee in employees.values():
    #https://www.geeksforgeeks.org/python-dictionary-values/
    if employee["gender"]=="male":
      males=males+1
    elif employee["gender"]=="female":
      females=females+1

  print("Number of male employees: ",males)
  print("Number of female employees: ",females)
  
def add_employee(): 
#to add new employee just add username,gender,and salary
  username=input("Enter employee's username: ")
  gender=input("Enter the gender: ")
  salary=input("Add the salary: ")

#id is incremented and the time is automatic

  emp_id = "emp{}".format(len(employees) + 1)

#https://www.tutorialspoint.com/how-to-add-timestamp-to-excel-file-in-python
  timestamp = datetime.datetime.now().strftime("%Y%m%d")
  employees[username] = {"emp_id": emp_id,"timestamp":timestamp,"gender": gender,"salary": salary}
  print("The user",username,"was added")

#display all the employees registered in the system ordered by date

def display_all_employees():
    sorted_employees = sorted(employees.items(), key=lambda x: x[1]["timestamp"], reverse=True)

    for username, employee in sorted_employees:
        emp_id = employee["emp_id"]
        timestamp = datetime.datetime.strptime(employee["timestamp"], "%Y%m%d").strftime("%Y-%m-%d")
        gender = employee["gender"]
        salary = employee["salary"]
    print("Id=",emp_id,",username=",username,",timestamp=",timestamp,",gender=",gender,",salary=",salary)


#change the employee's salary
def change_salary():
  emp_id=input("Enter the Id: ")
  salary=int(input("Enter the changed salary: "))
  if emp_id in employees:
        employees[emp_id]["salary"] = salary
        print("Salary changed successfully.")
    else:
        print("Id not found.")

# Remove employee from the data
def remove_employee():
    emp_id = input("Enter the Id: ")

    if emp_id in employees:
        del employees[emp_id]
        print("Employee removed successfully.")
    else:
        print("Id not found.")
  
# Raise employee's salary
def raise_salary():
    emp_id = input("Enter employee Id: ")
    percentage = float(input("Enter raise percentage: "))

    if emp_id in employees:
        employees[emp_id]["salary"] *= percentage
        print("Salary raised successfully.")
    else:
        print("Id not found.")

# Save employees to file
#https://www.w3schools.com/python/ref_file_write.asp
def save_employees():
    with open(employees.txt, "w") as file:
        for username, employee in employees.items():
            emp_id = employee["emp_id"]
            timestamp = employee["timestamp"]
            gender = employee["gender"]
            salary = employee["salary"]
            file.write(f"{emp_id},{username},{timestamp},{gender},{salary}\n")












def login_form(user_name,password):
  attempts=0

  while attempts<5:
    user_name=input("User name: ")
    password=input("Password: ")

  if user_name=="admin" and password=="admin123123":
    