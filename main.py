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
