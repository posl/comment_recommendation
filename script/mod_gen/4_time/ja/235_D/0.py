def main():
    a, n = map(int, input().split())
    count = 0
    while n > 1:
        if n % a == 0:
            n /= a
            count += 1
        elif n % 10 == 1:
            n = int(n / 10)
            count += 1
        else:
            count = -1
            break
    print(count)

if __name__ == '__main__':
    main()