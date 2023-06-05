def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            cnt += A[j]>>i&1
        ans += cnt*(N-cnt)*(1<<i)
        ans %= mod
    print(ans)
