def main():
    n = int(input())
    x = 0
    for i in range(1, n):
        x += i ** 2
        if x > n:
            print(i - 1)
            break

if __name__ == '__main__':
    main()