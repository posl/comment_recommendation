def check_honesty(persons, testimony):
    for i in range(len(persons)):
        if persons[i] == 1:
            if testimony[i] != 1:
                return False
    return True

if __name__ == '__main__':
    check_honesty()