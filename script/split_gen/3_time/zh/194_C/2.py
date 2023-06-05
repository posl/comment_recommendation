def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * A[i] * (N - 1)
    for i in range(N - 1):
        ans -= 2 * A[i] * sum(A[i + 1:])
    print(ans)
