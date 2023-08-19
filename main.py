
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
    print("/nAdmin Menu")
    print("1 to Display Statistics")
    print("2 to Add an Employee")
    print("3 Display all Employees")
    print("4 to Change Employee’s Salary")
    print("5 to Remove Employees")
    print("6 to Raise Employee’s Salary")
    print("7 to Save and Exit")
  

    choose=input("Enter your task number: ") #shoose whatever task they wanna make 

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
  













def login_form(user_name,password):
  attempts=0

  while attempts<5:
    user_name=input("User name: ")
    password=input("Password: ")

  if user_name=="admin" and password=="admin123123":
    