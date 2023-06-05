def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    if n == 2:
        print(1)
        return
    if n % 2 == 0:
        print(n * (n - 1) // 2)
    else:
        print((n - 1) * (n - 2) // 2 + n - 1)

if __name__ == '__main__':
    main()