def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        ans *= (min(B[i], max(A[i], B[i - 1])) - A[i] + 1)
        ans %= 998244353
    print(ans)
