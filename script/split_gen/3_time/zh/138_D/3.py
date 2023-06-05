def main():
    N, Q = map(int, input().split())
    ans = [0] * N
    for _ in range(N - 1):
        a, b = map(int, input().split())
        ans[a - 1] += 1
        ans[b - 1] += 1
    for _ in range(Q):
        p, x = map(int, input().split())
        ans[p - 1] += x
    print(*ans)
