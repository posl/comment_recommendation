def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i] * (i * (n - i - 1) + (i * (i - 1) // 2) + ((n - i - 1) * (n - i) // 2))
    print(ans)

if __name__ == '__main__':
    main()