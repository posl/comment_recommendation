def is_weak_password(x):
    if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
        return True
    elif (x[0] + 1) % 10 == x[1] and (x[1] + 1) % 10 == x[2] and (x[2] + 1) % 10 == x[3]:
        return True
    else:
        return False

if __name__ == '__main__':
    is_weak_password()