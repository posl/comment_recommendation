def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(N):
            if A[j] == i:
                ans[i] += 1
    for i in range(10):
        for j in range(1, N):
            ans[i] = ans[i] * (N - j) % MOD
    for i in range(10):
        print(ans[i])
