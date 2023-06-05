def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    n = 10
    a = [3, 14, 159, 2653, 58979, 323846, 2643383, 27950288, 419716939, 9375105820]
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] >> i & 1:
                cnt += 1
        ans += cnt * (n-cnt) * (1 << i)
        ans %= mod
    print(ans)
