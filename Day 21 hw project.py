#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add_employee(emp_id, emp_name, emp_DOJ, emp_designation, emp_salary):
    file1 = open('employee.txt', 'a')
    file2 = open('login.txt', 'a')
    emp = emp_id + ',' + emp_name + ',' + emp_DOJ + ',' + emp_designation + ',' + emp_salary + '\n'
    l = emp_name.split()
    emp_login = emp_id + ' ' + l[0] + '\n'
    file1.writelines(emp)
    file2.writelines(emp_login)
    file1.close()
    file2.close()
    return "Employee added Successfully"


def remove(emp_id, files, s):
    f = open(files, 'r')
    a = f.readlines()
    for i in range(len(a)):
        j = a[i].split(s)
        if j[0] == emp_id:
            a[i] = ''
            break
    f.close()
    f = open(files, 'w')
    f.writelines(a)
    f.close()


def remove_employee(emp_id):
    remove(emp_id, 'employee.txt', ',')
    remove(emp_id, 'hr.txt', ',')
    remove(emp_id, 'login.txt', ' ')


def check(emp_id):
    flag = False
    file = open("employee.txt", 'r')
    employee = file.readlines()
    for i in employee:
        j = i.split(',')
        if j[0] == emp_id:
            flag = True
    return flag


def add_hr(emp_id, hr_dept, hr_role):
    file = open('hr.txt', 'a')
    hr = emp_id + ',' + hr_dept + ',' + hr_role + '\n'
    file.writelines(hr)
    file.close()
    return "HR added successfully"


def remove_hr(emp_id):
    remove(emp_id, 'hr.txt', ',')


while 1:
    print("Welcome to admin!!")
    print("Enter 1 to add employee\nEnter 2 to remove employee\nEnter 3 to add hr\nEnter 4 to remove hr\nEnter q to "
          "exit")
    c = input("Enter your Option: ")
    if c == '1':
        emp_id = input("Employee ID - ")
        emp_name = input("Employee Name - ")
        emp_DOJ = input("Date of Joining - ")
        emp_designation = input("Designation: ")
        emp_salary = input("Salary: ")
        print(add_employee(emp_id, emp_name, emp_DOJ, emp_designation, emp_salary))
    elif c == '2':
        emp_id = input("Employee ID - ")
        remove_employee(emp_id)
    elif c == '3':
        emp_id = input("Employee ID - ")
        if (check(emp_id)):
            hr_dept = input("HR Department - ")
            hr_role = input("HR Role ")
            print(add_hr(emp_id, hr_dept, hr_role))
        else:
            print("Employee does not exist")
            break
    elif c == '4':
        emp_id = input("Employee ID - ")
        print("Is he leaving the company totally?")
        y = input("Enter yes or no: ")
        if y == 'yes':
            remove_employee(emp_id)
        else:
            remove_hr(emp_id)
    elif c == 'q':
        break


# In[ ]:


def check_hr(id):
    flag = False
    file = open("hr.txt", 'r')
    hr = file.readlines()
    for i in hr:
        j = i.split(',')
        if id == j[0]:
            flag = True
    return flag


def view_details(id):
    file = open("employee.txt", 'r')
    emp = file.readlines()
    for i in emp:
        j = i.split(',')
        if id == j[0]:
            return i
    else:
        return "Employee doesn't exist"


def view_employee(designation):
    file = open('employee.txt', 'r')
    emp = file.readlines()
    for i in emp:
        j = i.split(',')
        if designation == j[3]:
            print(i)
    return 0


def view_hr():
    file1 = open('hr.txt', 'r')
    file2 = open('employee.txt', 'r')
    hr = file1.readlines()
    emp = file2.readlines()
    for i in hr:
        for j in emp:
            k = i.split(',')
            l = j.split(',')
            if k[0] == l[0]:
                print(k[1] + ',' + l[1] + ',' + k[2])
                continue
    return 0


__name__ == '__main__'
id = input("Enter the id again: ")
if check_hr(id):
    while 1:
        print('enter 1 to view details\nenter 2 to view all employees\nenter q to exit')
        c = input("Enter your choice: ")
        if c == '1':
            print(view_details(id))
        elif c == '2':
            designation = input("Enter designation: ")
            view_employee(designation)
        elif c == 'q':
            break
else:
    while 1:
        print('enter 1 to view details\nenter 2 to view all HR names\nenter q to exit')
        c = input("Enter your choice: ")
        if c == '1':
            print(view_details(id))
        elif c == '2':
            view_hr()
        elif c == 'q':
            break


# In[ ]:


import sys
print("Welcome to Employee System")
id = input("Please Enter Login id:  ")
pwd = input("Please Enter Password:  ")
file = open("login.txt", "r")
a = file.readlines()
for i in a:
    b = i.split()
    if id == b[0] and pwd == b[1]:
        if id == 'admin':
            import admin
            break
        else:
            import employee
            break
else:
    print("Invalid id and password")
    sys.exit()


# In[ ]:





# In[ ]:




