def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(k):
        ans += (p[i] + 1) / 2
    now = ans
    for i in range(k, n):
        now += (p[i] + 1) / 2 - (p[i - k] + 1) / 2
        ans = max(ans, now)
    print(ans)
main()
