def check_follow(user1, user2, follow_list):
    if user1 in follow_list[user2] and user2 in follow_list[user1]:
        return True
    else:
        return False
