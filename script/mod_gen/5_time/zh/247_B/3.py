def check_name(name, names):
    for item in names:
        if item == name:
            return False
    return True

if __name__ == '__main__':
    check_name()