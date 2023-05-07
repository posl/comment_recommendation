def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    d1 = abs(r1 - c1)
    d2 = abs(r2 - c2)
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
        print(1)
        return
    if d1 == d2 or d1 % 2 == d2 % 2:
        print(2)
        return
    print(3)

if __name__ == '__main__':
    main()