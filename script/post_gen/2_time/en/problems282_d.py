Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    ans = 0
    for i in range(N):
        for j in G[i]:
            if j > i:
                ans += 1
                for k in G[j]:
                    if k > j:
                        if i not in G[k]:
                            ans += 1
    print(ans)
main()

I am not sure how to solve this problem. I have tried to use a 2D array to store the graph, but I am not sure how to do the second condition. Any help would be greatly appreciated.

Thanks

I am trying to write a program that will take a DNA sequence and find the longest common subsequence between the sequence and a list of sequences. I am having trouble with the longest common subsequence part. I have tried using dynamic programming and a recursive function but I am not getting the right result. I am not sure if I am doing it correctly. I am also not sure if I should be using dynamic programming or the recursive function.

Here is the code for the longest common subsequence using dynamic programming:

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if not visited[i]:
            q = [i]
            visited[i] = True
            while q:
                v = q.pop()
                for next_v in graph[v]:
                    if not visited[next_v]:
                        q.append(next_v)
                        visited[next_v] = True
            ans += 1
    print(ans - 1)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    color = [-1] * n
    ans = 0
    for i in range(n):
        if color[i] != -1:
            continue
        color[i] = 0
        q = [i]
        while q:
            v = q.pop()
            for nv in graph[v]:
                if color[nv] == -1:
                    color[nv] = 1 - color[v]
                    q.append(nv)
                elif color[nv] == color[v]:
                    print(0)
                    return
        cnt = [0, 0]
        for c in color:
            cnt[c] += 1
        ans += cnt[0] * cnt[1] - m
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N * (N - 1) // 2)
        return
    G = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        Q = [i]
        c = 0
        d = 0
        while Q:
            q = Q.pop()
            c += 1
            for j in G[q]:
                if visited[j]:
                    continue
                visited[j] = True
                Q.append(j)
                d += 1
        ans += c * d
    print(ans)

=======
Suggestion 5

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    # print(G)
    ans = 0
    for i in range(N):
        # print(i)
        color = [-1]*N
        color[i] = 1
        que = deque([i])
        while que:
            v = que.popleft()
            for nv in G[v]:
                if color[nv] == -1:
                    color[nv] = 1 - color[v]
                    que.append(nv)
                else:
                    if color[nv] == color[v]:
                        break
            else:
                continue
            break
        else:
            ans += color.count(0)
            continue
        break
    else:
        print(ans)
        return
    print(0)
    return

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort()
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            if edges[i][0] < edges[j][0] and edges[i][1] < edges[j][1]:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, M, *UV = map(int, read().split())
    UV = [u - 1 for u in UV]
    UV = [UV[2 * i:2 * (i + 1)] for i in range(M)]
    UV = sorted(UV)
    import bisect
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if [i, j] in UV:
                continue
            k = bisect.bisect_left(UV, [i, j])
            if k < M and UV[k][0] == i:
                continue
            l = bisect.bisect_left(UV, [j, i])
            if l < M and UV[l][0] == j:
                continue
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    if n == 2:
        print(0)
        return
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda x: x[0])
    ans = 0
    for i in range(m):
        u, v = edges[i]
        if u == v:
            continue
        if i == 0:
            ans += n - v
        else:
            if edges[i - 1][1] < v:
                ans += n - v
            else:
                ans += edges[i - 1][1] - v
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    # 2 <= N <= 2 * 10^5
    # 0 <= M <= min {2 * 10^5, N(N-1)/2 }
    # 1 <= u_i, v_i <= N
    # The graph G is simple.
    # All values in the input are integers.
    # The graph G is simple.

=======
Suggestion 10

def solve(N, M, edges):
    # Write your code here
    return 0
