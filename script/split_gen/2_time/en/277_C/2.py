def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ladders = [[] for _ in range(10**9+1)]
    for i in range(N):
        ladders[A[i]].append(B[i])
        ladders[B[i]].append(A[i])
    for i in range(1, 10**9+1):
        ladders[i].sort()
    q = deque()
    q.append(1)
    visited = [False]*(10**9+1)
    visited[1] = True
    while q:
        v = q.popleft()
        for w in ladders[v]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
    for i in range(10**9, 0, -1):
        if visited[i]:
            print(i)
            break
