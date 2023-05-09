def main():
    n = int(input())
    if n == 2:
        print(2)
        return
    for i in range(1, n):
        if i * (i + 1) >= n:
            print(i + n // i - 2)
            return

if __name__ == '__main__':
    main()