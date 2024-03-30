#task01: average of the salary
#task02: list of all employees name

# employees = [
#     {
#         "id": 101,
#         "name": "Jakaiya Masud",
#         "position": "System Engineer",
#         "salary": 40000
#     },
#     {
#         "id": 102,
#         "name": "Nusayba Jannat",
#         "position": "Network Administrator",
#         "salary": 45000
#     },
#     {
#         "id": 103,
#         "name": "Masum Billah",
#         "position": "Data Scientiest",
#         "salary": 70000
#     }
# ]

#task - 01
# total_salary = 0
# total_employee = 0
# for employee in employees:
#   total_salary += employee['salary']
#   total_employee += 1
  
# average_salary = total_salary / total_employee
# print("Average salary of each employee: ", average_salary)


#task - 02
# employee_names = []
# for employee in employees:
#   employee_names.append(employee['name'])
   
# print("List of all employee: ", employee_names)



#task - 01
# total_salary = sum([employee['salary'] for employee in employees])
# total_employee = len(employees)

# average_salary = total_salary / total_employee

# print("Average salary of each employee: ", average_salary)


#task - 02
# employee_names = [employee['name'] for employee in employees]
# print("List of all employee: ", employee_names)


















#syntax of function in python

# def display():

#     print('Hello, I am a function.')

# display()


#positional arguments/ required arguments, default arguments, veriable length argument/ non keyworded arguments, keyworded arguments

# def display(fname:str, lname:str):
#     message = 'Hello, {} {}'.format(fname, lname)

#     print(message)


# display("Sadiqul", "Islam")


#default arguments
# def display(fname:str, lname:str, mname=None):
#     if mname == None:
#         message = 'Hello, {0} {1}'.format(fname, lname, mname)
#         print(message)
#     else:
#         message = 'Hello, {0} {2} {1}'.format(fname, lname, mname)
#         print(message)


# fname = input('Enter your first name: ')
# mname = input('Enter your middle name: ')
# lname = input('Enter your last name: ')

# display(fname, lname, mname)


#variable length argument
# def add(*args):
#     sum = 0
#     for arg in args:
#         sum += arg

#     return sum

# result = add(1, 2, 3)

# print(result)


contacts = [
    
]

# {"name": "John", "email": "john@example.com", "address": "rampura, Dhaka."}


def create(**kwargs):
    contacts.append(kwargs)

name = input('Enter your name: ')
email = input('Enter your email: ')
message = input('Write message here ... ')


create(name=name, email=email, message=message)

print(contacts)
