def find_next_user(user):
    global users
    for u in users:
        if u[0] == user[1]:
            return u
    return None

if __name__ == '__main__':
    find_next_user()