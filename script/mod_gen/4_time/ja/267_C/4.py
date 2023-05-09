def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    C = [0] * (N + 1)
    for i in range(N + 1):
        C[i] = B[i] - i
    from collections import deque
    Q = deque()
    ans = -float("inf")
    for i in range(N + 1):
        while Q and Q[0][0] < i - M:
            Q.popleft()
        while Q and Q[-1][1] >= C[i]:
            Q.pop()
        Q.append((i, C[i]))
        ans = max(ans, C[i] - Q[0][1])
    print(ans)

if __name__ == '__main__':
    solve()