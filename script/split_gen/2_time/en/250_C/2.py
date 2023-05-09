def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    ans = [0] * N
    for i in range(N):
        ans[i] = i + 1
    for i in range(Q):
        x = X[i]
        ans[x - 1], ans[x] = ans[x], ans[x - 1]
    print(*ans)
