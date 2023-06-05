def main():
    a, b, c, d = map(int, input().split())
    if a < b:
        print(-1)
        return
    if d == 1:
        if a > b:
            print(1)
        else:
            print(0)
        return
    if b >= c * d:
        print(-1)
        return
    count = 1
    a -= b
    while True:
        if a <= c * d:
            print(count)
            return
        a -= c * d
        count += 1

if __name__ == '__main__':
    main()