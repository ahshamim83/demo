
users = [

]

def create_user(name: str, email: str, password: str) -> list[str]:
    user = {
        'name': name,
        'email': email,
        'password': password
    }

    users.append(user)

    return users


print(users)


    