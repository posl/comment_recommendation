def check_follow(user1, user2, follow_list):
    if user1 in follow_list[user2]:
        return True
    else:
        return False

if __name__ == '__main__':
    check_follow()