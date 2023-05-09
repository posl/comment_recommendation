def main():
    import sys
    from collections import deque
    N, K = map(int, sys.stdin.readline().split())
    P = list(map(int, sys.stdin.readline().split()))
    P = [p - 1 for p in P]
    ans = [-1] * N
    q = deque()
    for i, p in enumerate(P):
        while q and q[-1] <= p:
            q.pop()
        q.append(p)
        if i >= K - 1:
            ans[q[0]] = i + 1
            if q[0] == P[i - K + 1]:
                q.popleft()
    print(*ans, sep='
')

if __name__ == '__main__':
    main()