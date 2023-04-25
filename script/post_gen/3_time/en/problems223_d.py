Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    G = [[] for i in range(N)]
    for i in range(M):
        G[A[i] - 1].append(B[i] - 1)
    V = [0] * N
    P = []
    for i in range(N):
        if V[i] == 0:
            if not dfs(i, G, V, P):
                print(-1)
                return
    P = P[::-1]
    print(*[x + 1 for x in P])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, M)
    #print(A)
    #print(B)
    ans = []
    ans.append(1)
    for i in range(2, N+1):
        ans.append(i)
    #print(ans)
    for i in range(M):
        for j in range(N-1):
            if A[i] == ans[j] and B[i] == ans[j+1]:
                tmp = ans[j+1]
                ans[j+1] = ans[j]
                ans[j] = tmp
    #print(ans)
    for i in range(M):
        for j in range(N-1):
            if A[i] == ans[j] and B[i] == ans[j+1]:
                print("-1")
                return
    print(*ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(N, M)
    # print(A)
    # print(B)
    # 1. トポロジカルソート
    # 2. トポロジカルソートできるか判定
    # 3. トポロジカルソートを実行
    # 4. トポロジカルソートの結果を出力

    # 1. トポロジカルソート
    # 2. トポロジカルソートできるか判定
    # 3. トポロジカルソートを実行
    # 4. トポロジカルソートの結果を出力

    # 1. トポロジカルソート
    # 2. トポロジカルソートできるか判定
    # 3. トポロジカルソートを実行
    # 4. トポロジカルソートの結果を出力

    # 1. トポロジカルソート
    # 2. トポロジカルソートできるか判定
    # 3. トポロジカルソートを実行
    # 4. トポロジカルソートの結果を出力

    # 1. トポロジカルソート
    # 2. トポロジカルソートできるか判定
    # 3. トポロジカルソートを実行
    # 4. トポロジカルソートの結果を出力

    # 1. トポロジカルソート
    # 2.

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N)]
    for A, B in AB:
        A -= 1
        B -= 1
        G[A].append(B)
    ans = []
    done = [False] * N
    for i in range(N):
        if done[i]:
            continue
        done[i] = True
        stack = [i]
        while stack:
            v = stack.pop()
            ans.append(v)
            for nv in G[v]:
                if done[nv]:
                    print(-1)
                    return
                done[nv] = True
                stack.append(nv)
    print(*[v + 1 for v in ans])

main()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
    ans = [-1]*N
    for i in range(N):
        if ans[i] == -1:
            ans[i] = i+1
            for j in G[i]:
                if ans[j] == -1:
                    ans[j] = i+1
                else:
                    print(-1)
                    return
    print(*ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])

    P = [-1] * (N + 1)
    for a, b in AB:
        if P[b] == -1:
            P[b] = a
        elif P[b] != a:
            print(-1)
            return

    for i in range(1, N + 1):
        if P[i] == -1:
            P[i] = i
        else:
            P[i] = P[P[i]]

    print(*P[1:])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0] * N
    for a, b in AB:
        if ans[a-1] == 0 and ans[b-1] == 0:
            ans[a-1] = b
            ans[b-1] = a
        elif ans[a-1] != 0:
            ans[ans[a-1]-1] = b
            ans[b-1] = ans[a-1]
            ans[a-1] = b
        elif ans[b-1] != 0:
            ans[ans[b-1]-1] = a
            ans[a-1] = ans[b-1]
            ans[b-1] = a
    for i in range(N):
        if ans[i] == 0:
            ans[i] = i+1
    if len(set(ans)) == len(ans):
        print(*ans)
    else:
        print(-1)

=======
Suggestion 8

def main():
    # 入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    # 隣接リスト
    adj = [[] for _ in range(N)]
    for a, b in AB:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    # トポロジカルソート
    ans = []
    visited = [False] * N
    for i in range(N):
        if visited[i]:
            continue
        stack = [i]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            for w in adj[v]:
                if visited[w]:
                    continue
                stack.append(w)
            ans.append(v)

    # 出力
    if len(ans) == N:
        print(*[a + 1 for a in ans])
    else:
        print(-1)

=======
Suggestion 9

def find_smallest_permutation(n, m, a, b):
    ans = []
    g = [[] for _ in range(n)]
    for i in range(m):
        g[a[i]-1].append(b[i]-1)
        g[b[i]-1].append(a[i]-1)
    used = [False] * n
    for i in range(n):
        if not used[i]:
            used[i] = True
            que = [i]
            while que:
                v = que.pop()
                ans.append(v+1)
                for to in g[v]:
                    if not used[to]:
                        used[to] = True
                        que.append(to)
    if len(ans) != n:
        return -1
    else:
        return ans

n, m = map(int, input().split())
a = []
b = []
for i in range(m):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)
ans = find_smallest_permutation(n, m, a, b)
