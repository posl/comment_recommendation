def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    d = {}
    for i in range(N):
        m = A[i] % mod
        if m in d:
            d[m] += 1
        else:
            d[m] = 1
    ans = 0
    for k, v in d.items():
        if v >= 2:
            ans += v * (v - 1) // 2
    print(ans)
