def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + [i % m for i in a]
    for i in range(1, n + 1):
        a[i] += a[i - 1]
        a[i] %= m
    b = [0 for i in range(m)]
    for i in a:
        b[i] += 1
    ans = 0
    for i in b:
        ans += i * (i - 1) // 2
    print(ans)
main()
