def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    d = abs(r2 - r1) + abs(c2 - c1)
    if d == 0:
        print(0)
    elif d <= 3 or (d % 2 == 0) or (abs(r2 - c2) - abs(r1 - c1)) % 2 == 0:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()