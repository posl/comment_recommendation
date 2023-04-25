Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    bridges = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        bridges[a - 1].add(b - 1)
        bridges[b - 1].add(a - 1)
    print(N - 1 - max(len(bridge) for bridge in bridges))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    ans = 0
    prev = 0
    for a, b in bridges:
        if prev < a:
            ans += 1
            prev = b - 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    bridge = [0] * (N + 1)
    for a, b in AB:
        if bridge[a] == 0:
            bridge[a] = 1
            bridge[b] = 1
            ans += 1
    print(M - ans)
main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    count = 0
    last = 0
    for a, b in bridges:
        if last < a:
            last = b - 1
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    while bridges:
        a, b = bridges.pop()
        ans += 1
        while bridges and bridges[-1][0] >= a:
            bridges.pop()
    print(ans)

=======
Suggestion 6

def find(x):
    if x == p[x]:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        visited = [False] * (N + 1)
        visited[edges[i][0]] = True
        visited[edges[i][1]] = True
        for j in range(M):
            if j == i:
                continue
            if visited[edges[j][0]] and visited[edges[j][1]]:
                continue
            visited[edges[j][0]] = True
            visited[edges[j][1]] = True
        if not all(visited):
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    from sys import stdin
    from bisect import bisect_left
    from collections import deque
    readline = stdin.readline
    N, M = map(int, readline().split())
    bridge = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, readline().split())
        bridge[a].append(b)
        bridge[b].append(a)
    for i in range(1, N+1):
        bridge[i].sort()
    visited = [False] * (N+1)
    visited[1] = True
    q = deque([1])
    count = 0
    while q:
        v = q.popleft()
        for w in bridge[v]:
            if not visited[w]:
                visited[w] = True
                count += 1
                q.append(w)
    print(M - count)

=======
Suggestion 9

def main():
    from sys import stdin
    from bisect import bisect_left
    from collections import defaultdict

    N, M = map(int, stdin.readline().split())
    bridges = defaultdict(list)
    for _ in range(M):
        a, b = map(int, stdin.readline().split())
        bridges[a].append(b)
        bridges[b].append(a)
    for k, v in bridges.items():
        bridges[k] = sorted(v)

    ans = 0
    for i in range(1, N+1):
        for j in bridges[i]:
            if i < j:
                ans += 1
                bridges[j].pop(bisect_left(bridges[j], i))
    print(ans)

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    requests = [list(map(int,input().split())) for _ in range(m)]
    requests.sort(key=lambda x: x[1])
    removed = 0
    last = 0
    for a,b in requests:
        if a > last:
            removed += 1
            last = b-1
    print(removed)
