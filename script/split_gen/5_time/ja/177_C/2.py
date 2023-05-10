def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(N - 1):
        sum -= A[i]
        ans += sum * A[i]
        ans %= MOD
    print(ans)
