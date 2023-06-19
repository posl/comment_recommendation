def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & (1 << i):
                cnt += 1
        ans += (1 << i) * (cnt * (n - cnt))
        ans %= (10 ** 9 + 7)
    print(ans)
main()
