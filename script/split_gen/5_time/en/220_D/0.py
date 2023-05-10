def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        ans[i] = 1 if i == A[-1] else 0
    for i in range(N-2, -1, -1):
        tmp = [0] * 10
        for j in range(10):
            tmp[(j + A[i]) % 10] = (tmp[(j + A[i]) % 10] + ans[j]) % MOD
            tmp[(j * A[i]) % 10] = (tmp[(j * A[i]) % 10] + ans[j]) % MOD
        ans = tmp
    print(*ans, sep="\n")
