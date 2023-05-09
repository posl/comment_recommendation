def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    sum = 0
    for i in range(N):
        sum += A[i]
    ans = 0
    for i in range(N):
        sum -= A[i]
        ans += A[i] * sum % mod
    print(ans % mod)
