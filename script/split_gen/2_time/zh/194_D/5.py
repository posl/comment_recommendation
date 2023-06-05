def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += (n - 1) * a[i] ** 2
    for i in range(n - 1):
        ans -= 2 * a[i] * sum(a[i + 1:])
    print(ans)
main()
