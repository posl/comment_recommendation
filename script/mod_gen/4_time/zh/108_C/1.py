def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        ans += n // i * max(0, (i - k))
        ans += max(0, (n % i + 1 - k))
    print(ans)

if __name__ == '__main__':
    main()