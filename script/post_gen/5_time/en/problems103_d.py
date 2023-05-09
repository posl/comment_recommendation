Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    A.append(N+1)
    B.append(N+1)
    ans = 0
    j = 0
    for i in range(1, N+2):
        while A[j] < i:
            j += 1
        ans = max(ans, j - i + 1)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    a = []
    b = []
    for i in range(M):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    if a[0] < b[0]:
        print(b[0] - a[-1])
    else:
        print(a[0] - b[-1])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 1
    r = AB[0][1]
    for a, b in AB:
        if a <= r:
            continue
        ans += 1
        r = b
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 1
    bridge = AB[0][1]
    for i in range(1, M):
        if AB[i][0] <= bridge:
            continue
        ans += 1
        bridge = AB[i][1]
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    right = -1
    for i in range(M):
        if AB[i][0] > right:
            ans += 1
            right = AB[i][1]
    print(ans)

=======
Suggestion 6

def solve():
    #import sys
    #input = sys.stdin.readline
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort(key=lambda x: x[1])
    ans = 0
    right = -1
    for a, b in ab:
        if a > right:
            ans += 1
            right = b - 1
    print(ans)
    return 0

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[0])
    ab.sort(key=lambda x: x[1])
    print(ab)
    count = 0
    for i in range(m-1):
        if ab[i][1] > ab[i+1][0]:
            count += 1
    print(count)

=======
Suggestion 8

def dfs(v):
    visited[v] = True
    for i in G[v]:
        if not visited[i]:
            dfs(i)

N,M = map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

visited = [False]*N
ans = 0
for i in range(N):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans-1)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(M)]
    
    ab.sort(key=lambda x: x[1])
    ans = 0
    last = -1
    for a, b in ab:
        if a > last:
            ans += 1
            last = b - 1
    print(ans)

=======
Suggestion 10

def main():
    import sys
    from collections import defaultdict
    from collections import deque
    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = defaultdict(set)

    for _ in range(m):
        a, b = map(int, input().split())
        d[a].add(b)
        d[b].add(a)

    visited = [False] * (n + 1)
    cnt = 0
    for i in range(1, n + 1):
        if visited[i]:
            continue
        q = deque([i])
        visited[i] = True
        while q:
            cur = q.popleft()
            for nxt in d[cur]:
                if visited[nxt]:
                    continue
                visited[nxt] = True
                q.append(nxt)
        cnt += 1

    print(cnt - 1)
