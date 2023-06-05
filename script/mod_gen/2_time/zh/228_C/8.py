def check_friend(friends, friend_id, secret_owner):
    if friend_id == secret_owner:
        return True
    elif friends[friend_id] == secret_owner:
        return True
    else:
        return check_friend(friends, friends[friend_id], secret_owner)

if __name__ == '__main__':
    check_friend()