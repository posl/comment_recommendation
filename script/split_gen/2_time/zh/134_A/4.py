def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(1, N):
        ans[i] = 2 * A[i - 1] - ans[i - 1]
    ans[0] = 2 * A[N - 1] - ans[N - 1]
    print(*ans)
