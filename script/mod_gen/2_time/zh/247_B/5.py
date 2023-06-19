def check_name(name, names):
    for n in names:
        if name == n:
            return False
    return True

if __name__ == '__main__':
    check_name()