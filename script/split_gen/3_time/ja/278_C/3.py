def follow(user1, user2):
    if user1 == user2:
        return False
    if user1 in users[user2]:
        return True
    return False
