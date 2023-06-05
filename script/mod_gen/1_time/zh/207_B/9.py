def main():
    a, b, c, d = map(int, input().split())
    if a < b * d:
        print(-1)
        return
    if b * d <= c:
        print(-1)
        return
    count = 0
    while True:
        if a <= b * d:
            break
        a += b
        a -= c
        count += 1
    print(count)

if __name__ == '__main__':
    main()