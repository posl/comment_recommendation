def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (N - i - 1)
        ans += A[i] * i
    ans *= K
    ans %= 1000000007
    print(ans)
