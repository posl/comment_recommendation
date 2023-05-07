def main():
    x, y = map(int, input().split())
    if (x + y) % 3 == 0:
        print(0)
    elif (x + y) % 3 == 1:
        print(1)
    else:
        print(2)
