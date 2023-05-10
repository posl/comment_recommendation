def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i] ** 2 * (n - 1)
    for i in range(1, n):
        ans -= 2 * a[i - 1] * sum(a[i:])
    print(ans)

if __name__ == '__main__':
    main()