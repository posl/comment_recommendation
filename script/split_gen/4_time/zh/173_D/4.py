def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    for i in range(2 * N - 1):
        A[i + 1] += A[i]
    ans = 0
    for i in range(N):
        ans = max(ans, A[i + N - 1] - A[i])
    print(ans)
