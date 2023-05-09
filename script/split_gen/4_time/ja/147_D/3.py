def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        count = 0
        for j in range(N):
            if A[j] & 1:
                count += 1
            A[j] >>= 1
        ans += count*(N-count)*pow(2,i,MOD)
        ans %= MOD
    print(ans)
