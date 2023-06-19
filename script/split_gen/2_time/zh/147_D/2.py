def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    mod = 10**9 + 7
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] >> i & 1:
                cnt += 1
        ans += (cnt * (N - cnt) * (1 << i)) % mod
    print(ans % mod)
