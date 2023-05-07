def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += A[i] * (N-i-1) * A[i+1]
        ans %= 10**9 + 7
    print(ans)
