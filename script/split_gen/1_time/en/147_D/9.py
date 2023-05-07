def XOR_sum(N, A):
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] >> i & 1:
                cnt += 1
        ans += (cnt * (N-cnt) * (1 << i)) % mod
    return ans % mod
N = int(input())
A = list(map(int, input().split()))
print(XOR_sum(N, A))
