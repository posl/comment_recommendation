def main():
    import sys
    from collections import deque
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, K = map(int, readline().split())
    P = list(map(int, readline().split()))
    P = [p-1 for p in P]
    D = deque(P)
    ans = [-1]*N
    for i in range(N):
        p = D.popleft()
        ans[p] = i+1
        if i+1 >= K:
            break
    for i in range(N):
        p = P[i]
        if ans[p] == -1:
            ans[p] = ans[D[0]] + K
    print(*ans, sep='
')
