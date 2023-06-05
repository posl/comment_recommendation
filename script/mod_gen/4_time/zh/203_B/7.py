def main():
    n, k = map(int, input().split())
    print((100 * n + 10 * k + 3) * n * k // 2)

if __name__ == '__main__':
    main()