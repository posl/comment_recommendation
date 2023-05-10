def main():
    n = int(input())
    if n < 10:
        print(n)
        return
    a = int(n ** (1 / 3))
    for i in range(a, 0, -1):
        if n % i == 0:
            b = int(n / i)
            if i ** 3 + i ** 2 * b + i * b ** 2 + b ** 3 == n:
                print(i + b)
                return
    print(n)

if __name__ == '__main__':
    main()