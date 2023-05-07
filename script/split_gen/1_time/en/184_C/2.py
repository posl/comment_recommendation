def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    d = abs(r1 - r2) + abs(c1 - c2)
    if d == 0:
        print(0)
    elif d <= 3:
        print(1)
    elif (d % 2 == 0) or (d <= 6):
        print(2)
    else:
        print(3)
