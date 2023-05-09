def main():
    n, m = map(int, input().split())
    for i in range(n):
        print(*[min((i - j) ** 2 + (i - k) ** 2, (n - 1 - j) ** 2 + (i - k) ** 2, (j - 0) ** 2 + (n - 1 - k) ** 2, (n - 1 - j) ** 2 + (n - 1 - k) ** 2) for j in range(n) for k in range(n) if (i - j) ** 2 + (i - k) ** 2 == m or (n - 1 - j) ** 2 + (i - k) ** 2 == m or (j - 0) ** 2 + (n - 1 - k) ** 2 == m or (n - 1 - j) ** 2 + (n - 1 - k) ** 2 == m], sep=' ')
main()

if __name__ == '__main__':
    main()