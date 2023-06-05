def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    maxA = [0] * N
    maxA[0] = A[0]
    for i in range(1, N):
        maxA[i] = max(maxA[i - 1], A[i])
    minA = [0] * N
    minA[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        minA[i] = min(minA[i + 1], A[i])
    ans = 0
    for i in range(N):
        if (minA[i] <= P and P <= maxA[i] and minA[i] <= Q - P and Q - P <= maxA[i] and minA[i] <= R - Q + P and R - Q + P <= maxA[i]):
            ans += 1
    if ans > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()