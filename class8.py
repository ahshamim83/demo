import addition
from users import objects

print(addition.add(2, 3))


name = input('enter your name: ')
email = input('enter your email: ')
password = input('enter your password: ')

users = objects.create_user(name, email, password)

if len(users) == 0:
    print('Something went wrong.Please try again')

else:
    print(users)
    print('Congratulations! You have successfully created a new user.')