def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    elif x == 0 and y == 1:
        print(2)
    elif x == 1 and y == 2:
        print(0)
    elif x == 2 and y == 0:
        print(1)
    elif y == 0 and x == 1:
        print(2)
    elif y == 1 and x == 2:
        print(0)
    elif y == 2 and x == 0:
        print(1)
