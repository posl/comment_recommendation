def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    ans = 0
    for i in range(N-1):
        ans += A[i]*(A[i+1]*i - A[i]*(N-1-i))
        ans %= 10**9+7
    print(ans)
