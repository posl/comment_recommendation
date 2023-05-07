def main():
    a, n = map(int, input().split())
    count = 0
    while n != 1:
        if n % a == 0:
            n = n // a
            count += 1
        elif n % 10 == 0:
            n = n // 10
            count += 1
        else:
            n = (n % 10) * (10 ** (len(str(n)) - 1)) + (n // 10)
            count += 1
    print(count)

if __name__ == '__main__':
    main()