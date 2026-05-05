users = {
    "Anton": 1000,
    "Ivan": 2500,
    "Maria": 200,
    "Stas": 1000,
}

def get_average_balance(users):
    return sum(users.values()) / len(users)


print(get_average_balance(users))


def empty_user(users):
    empty_user = []
    for name, balance in users.items():
        if balance == 0:
            empty_user.append(name)
    return empty_user

print(empty_user(users))