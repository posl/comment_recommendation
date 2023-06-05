def main():
    a, n = map(int, input().split())
    if n % a != 0:
        n = n * a
    else:
        n = n // a
    if n % 10 != 0:
        print(-1)
        return
    n = n // 10
    count = 1
    while n > 1:
        if n % 10 == 0:
            n = n // 10
            count += 1
        else:
            print(-1)
            return
    print(count)

if __name__ == '__main__':
    main()