def main():
    x, y = map(int, input().split('.'))
    if y <= 2:
        print(str(x) + '-')
    elif y >= 3 and y <= 6:
        print(x)
    else:
        print(str(x) + '+')
