def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    que = deque()
    for i in range(N):
        while que and que[-1][1] >= P[i]:
            que.pop()
        que.append((i, P[i]))
        if i >= K - 1:
            ans[i] = que[0][1]
        if que[0][0] == i - K + 1:
            que.popleft()
    print(*ans, sep='\n')
