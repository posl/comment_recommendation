def check_follow(user, follow):
    if user in follow:
        return True
    else:
        return False

if __name__ == '__main__':
    check_follow()