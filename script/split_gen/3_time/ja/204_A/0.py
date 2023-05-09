def main():
    x, y = map(int, input().split())
    if x == 0:
        if y == 0:
            print(0)
        elif y == 1:
            print(2)
        else:
            print(1)
    elif x == 1:
        if y == 0:
            print(1)
        elif y == 1:
            print(0)
        else:
            print(2)
    elif x == 2:
        if y == 0:
            print(2)
        elif y == 1:
            print(1)
        else:
            print(0)
