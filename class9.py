#sadiq
# from users.sub_pack import dev
# from users import sub_pack
# import users.sub_pack as s
# import module
from users.sub_pack.dev import create_account
from users.sub_pack.dev import *



name = input('Enter your name: ')
age = int(input('Enter your age please: '))
password = input('Set a strong password: ')


# result = dev.create_account(name, age, password)
# result = sub_pack.dev.create_account(name, age, password)
result = create_account(name, age, password)

print(result)