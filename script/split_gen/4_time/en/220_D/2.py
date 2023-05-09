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
        ans[i] %= MOD
    for i in range(10):
        for j in range(10):
            if i + j < 10:
                ans[i + j] += ans[i] * ans[j]
                ans[i + j] %= MOD
            else:
                ans[i + j - 10] += ans[i] * ans[j]
                ans[i + j - 10] %= MOD
    for i in range(10):
        print(ans[i])
