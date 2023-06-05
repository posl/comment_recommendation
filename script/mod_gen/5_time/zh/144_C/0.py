def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    for i in range(2, n):
        if n % i == 0:
            print(i + int(n / i) - 2)
            return

if __name__ == '__main__':
    main()