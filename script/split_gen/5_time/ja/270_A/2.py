def main():
    a, b = map(int, input().split())
    if a != 0 and b != 0:
        print(3)
    elif a != 1 and b != 1:
        print(1)
    elif a != 2 and b != 2:
        print(2)
    else:
        print(0)
