def main():
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x == 0 and y == 1:
        print(2)
    elif x == 0 and y == 2:
        print(0)
    elif x == 1 and y == 0:
        print(0)
    elif x == 1 and y == 2:
        print(1)
    elif x == 2 and y == 0:
        print(1)
    elif x == 2 and y == 1:
        print(2)
    else:
        print(x)
