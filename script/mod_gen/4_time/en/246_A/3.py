def problem246_a():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if x1 == x2:
        print(x3, y3)
    elif x1 == x3:
        print(x2, y2)
    elif x2 == x3:
        print(x1, y1)

if __name__ == '__main__':
    problem246_a()