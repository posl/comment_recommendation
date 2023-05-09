def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(N):
        ans += (B[i] * (B[i] + 1) // 2) - (A[i] * (A[i] - 1) // 2)
    print(ans % mod)
