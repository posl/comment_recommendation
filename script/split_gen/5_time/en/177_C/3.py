def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(N):
        ans += A[i] * sum(A[i+1:])
    print(ans % mod)
