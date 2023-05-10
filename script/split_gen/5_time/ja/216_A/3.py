def main():
    x, y = map(int, input().split('.'))
    if y <= 2:
        print(x, '-')
    elif y <= 6:
        print(x)
    else:
        print(x, '+')
