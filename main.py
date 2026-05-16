from dbm import error

users = {
    "Anton": 1000,
    "Ivan": 2500,
    "Maria": 200,
    "Stas": 0,
}


def get_average_balance(users):
    return sum(users.values()) / len(users)


print(get_average_balance(users))


def get_empty_user(users):
    empty_user = []
    for name, balance in users.items():
        if balance == 0:
            empty_user.append(name)
    return empty_user


print(get_empty_user(users))


def poor_users(users, threshold):
    poor_users = []
    for name, balance in users.items():
        if balance < threshold:
            poor_users.append(name)
    return poor_users


print(poor_users(users, 1000))


def analyze_users(users):
    result = {
        "total_users": 0,
        "average_balance": 0,
        "richest_users": None,
        "poor_users": [],
    }

    richest_balance = None
    richest_name = None

    for name, balance in users.items():
        if richest_balance is None or balance > richest_balance:
            richest_balance = balance
            richest_name = name

    result = {
        "total_users": len(users),
        "average_balance": get_average_balance(users),
        "richest_user": richest_name,
        "poor_users": poor_users(users, 1000),
    }
    return result


users = {
    "Anton": 1000,
    "Ivan": 2500,
    "Maria": 200,
    "Stas": 0,
}


def get_average_balance(users):
    return sum(users.values()) / len(users)


print(get_average_balance(users))


def get_empty_user(users):
    empty_user = []
    for name, balance in users.items():
        if balance == 0:
            empty_user.append(name)
    return empty_user


print(get_empty_user(users))


def poor_users(users, threshold):
    poor_users = []
    for name, balance in users.items():
        if balance < threshold:
            poor_users.append(name)
    return poor_users


print(poor_users(users, 1000))


def analyze_users(users):
    # result = {
    #     "total_users": 0,
    #     "average_balance": 0,
    #     "richest_users": None,
    #     "poor_users": [],
    # }

    richest_balance = None
    richest_name = None

    for name, balance in users.items():
        if richest_balance is None or balance > richest_balance:
            richest_balance = balance
            richest_name = name

    result = {
        "total_users": len(users),
        "average_balance": get_average_balance(users),
        "richest_user": richest_name,
        "poor_users": poor_users(users, 1000),
    }
    return result


print(analyze_users(users))


def get_users_stats(users):
    vip_count = 0
    low_count = 0
    empty_count = 0
    for name, balance in users.items():
        if balance > 2000:
            vip_count += 1
        elif balance == 0:
            empty_count += 1
        elif balance < 1000:
            low_count += 1

    stats = {
        "vip_count": vip_count,
        "low_count": low_count,
        "empty_count": empty_count,
    }
    return stats


print(get_users_stats(users))


def get_user_total_balance(users):
    result = {}
    for name, balance in users.items():
        result[name] = balance + 100

    return result


print(get_user_total_balance(users))

users = {
    "Anton": {"balance": 1000, "city": "Moscow"},
    "Ivan": {"balance": 2500, "city": "Sochi"},
    "Maria": {"balance": 200, "city": "Moscow"},
}


def get_user_from_city(users, city):
    result = []
    for key, value in users.items():
        if value["city"] == city:
            result.append(key)
    return result


print(get_user_from_city(users, "Moscow"))


def get_total_user_balance(users, city):
    total_balance = 0
    for name, value in users.items():
        if value["city"] == city:
            total_balance += value["balance"]
    return total_balance


print(get_total_user_balance(users, "Moscow"))


def get_richest_balance(users, theshold):
    richest_users = []
    for name, balance in users.items():
        if balance["balance"] > theshold:
            richest_users.append(name)
    return richest_users


print(get_richest_balance(users, 1000))


def add_bonus(users, city, bonus):
    for name, balance in users.items():
        if balance["city"] == city:
            balance["balance"] += bonus


print(add_bonus(users, "Moscow", 500))
print(users)


def transfer_money(users, from_users, to_users, amount):
    if from_users not in users or to_users not in users:
        return {
            "status": "error",
            "message": "users not found"
        }
    elif users[from_users]["balance"] < amount:

        return {
            "status": "error",
            "message": "low Money"
        }
    else:
        users[from_users]["balance"] -= amount
        users[to_users]["balance"] += amount
    return {
        "status": "success",
        "message": f"{from_users} transfer -> {amount} to {to_users}"}


print(transfer_money(users, "Ivan", "Anton", 500))
print(users)


def divide_balance(balance, part):
    try:
        result = balance / part
        return {
            "status": "success",
            "result": result}
    except ZeroDivisionError:
        return {"status": "error",
                "message": "division by zero"}


print(divide_balance(1000, 2))
print(divide_balance(1000, 0))


def test():
    try:
        print("start")
        x = 10 / 0
    except ZeroDivisionError:
        print("error")
    finally:
        print("finish")


test()


def safe_withdraw(balance, amount):
    try:
        if balance < amount:
            raise ValueError("low Balance")
        result = balance - amount
        return {"status": "success",
                "result": result}
    except ValueError as e:
        return {"status": "error",
                "message": f"{e}"}
    finally:
        print("operation finished")


print(safe_withdraw(1000, 2))
print(safe_withdraw(1000, 0))
print(safe_withdraw(1000, 1200))
