def main():
    n, k = map(int, input().split())
    print((n * (n + 1) * k * (k + 1)) // 4)

if __name__ == '__main__':
    main()