def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * 10
    for i in range(10):
        ans[i] = pow(2, N - 1, 998244353)
        for j in range(N):
            if A[j] == i:
                ans[i] -= pow(2, N - j - 1, 998244353)
    for i in range(10):
        print(ans[i] % 998244353)
