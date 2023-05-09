def check_honesty(persons, a, x, y):
    for i in range(a):
        if (y[i] == 1):
            persons[x[i] - 1] = 1
        else:
            if (persons[x[i] - 1] == 1):
                return False
    return True

if __name__ == '__main__':
    check_honesty()