#zulfiker

customers = []

def create_account(name: str, age: int,  password: str) -> str:
    kwargs = {
        'name': name,
        'age': age,
        'password': password
    }

    customers.append(kwargs)
    message = 'Successfully created  your account.'
    return message


print(__name__)

if __name__ == '__main__':

    name = input('Enter your name: ')
    age = int(input('Enter your age please: '))
    password = input('Set a strong password: ')


    result = create_account(name, age, password)

    print(result)