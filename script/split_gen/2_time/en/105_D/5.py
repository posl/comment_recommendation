def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] %= m
    sum = [0] * (n + 1)
    for i in range(n):
        sum[i + 1] = (sum[i] + a[i]) % m
    sum.sort()
    ans = 0
    cnt = 1
    for i in range(n):
        if sum[i] == sum[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)
