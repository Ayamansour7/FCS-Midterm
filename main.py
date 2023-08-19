file = open("employees.txt", "r")
#https://www.freecodecamp.org/news/python-import-from-file-importing-local-files-in-python/

def admin_menu():
  while True:
    print("1 to Display Statistics")
    print("2 to Add an Employee")
    print("3 Display all Employees")
    print("4 to Change Employee’s Salary")
    print("5 to Remove Employees")
    print("6 to Raise Employee’s Salary")
    print("7 to Save and Exit")
  

    choose=input("Enter your task number: ")

    if choose=="1":
      show_statistics()
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
      save_exit()
    else:
      print("Task not valid")


def login_form(user_name,password):
  attempts=0

  while attempts<5:
    user_name=input("User name: ")
    password=input("Password: ")

  if user_name=="admin" and password=="admin123123":
    