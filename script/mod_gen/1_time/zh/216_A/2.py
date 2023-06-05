def problem216_a():
    x, y = map(int, input().split('.'))
    if 0 <= y <= 2:
        print(x, '-')
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(x, '+')

if __name__ == '__main__':
    problem216_a()