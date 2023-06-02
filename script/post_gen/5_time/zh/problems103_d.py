Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    ab = sorted(ab,key=lambda x:x[1])
    ans = 1
    right = ab[0][1]
    for i in range(1,m):
        if ab[i][0] >= right:
            ans += 1
            right = ab[i][1]
    print(ans)

=======
Suggestion 2

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    a = [0] * M
    b = [0] * M
    for i in range(M):
        a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    G = [[] for _ in range(N)]
    for i in range(M):
        G[a[i]].append(b[i])
        G[b[i]].append(a[i])
    V = [False] * N
    def dfs(v):
        V[v] = True
        for i in range(len(G[v])):
            if V[G[v][i]] == False:
                dfs(G[v][i])
    ans = 0
    for i in range(N):
        if V[i] == False:
            dfs(i)
            ans += 1
    print(ans - 1)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

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
    i = 0
    j = 0
    count = 0
    while i < N and j < N:
        if a[i] == j + 1:
            i += 1
        elif b[j] == i + 1:
            j += 1
        else:
            count += 1
            i += 1
            j += 1
    print(count)

=======
Suggestion 6

def main():
    N, M = [int(x) for x in input().split()]
    a = []
    b = []
    for i in range(M):
        a_i, b_i = [int(x) for x in input().split()]
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    print(min(a[0]-1, N-b[-1], b[0]-a[-1], N-a[0]))

=======
Suggestion 7

def dfs(i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)

N,M=map(int,input().split())
graph=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
visited=[False]*N
ans=0
for i in range(N):
    if not visited[i]:
        dfs(i)
        ans+=1
print(ans-1)

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    a = []
    b = []
    for i in range(M):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()

    ans = 0
    for i in range(N-1):
        if a[-1] <= i+1 and i+1 <= b[0]:
            ans += 1

    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    a = [0] * M
    b = [0] * M
    for i in range(M):
        a[i], b[i] = map(int, input().split())
    # 从西边来的第i个岛和从西边来的第（i+1）个岛之间发生了争端
    # 从西边来的第a_i个岛和从西边来的第b_i个岛之间发生了争端
    # 拆除一些桥梁以满足所有这些M请求
    # 找出必须拆除的最小桥梁数量
    # 从西边来的第i个岛和从西边来的第（i+1）个岛之间发生了争端
    # 从西边来的第a_i个岛和从西边来的第b_i个岛之间发生了争端
    # 可以拆除的桥梁数量
    # 从第1个岛开始，逐个检查是否可以拆除
    # 拆除的桥梁数量
    # 检查第i个岛和第（i+1）个岛之间是否可以拆除
    # 检查第a_i个岛和第b_i个岛之间是否可以拆除
    # 检查第i个岛和第（i+1）个岛之间是否可以拆除
    # 检查第a_i个岛和第b_i个岛之间是否可以拆除
    # 拆除的桥梁数量
    # 检查第i个岛和第（i+1）个岛之间是否可以拆除
    # 检查第a_i个岛和第b_i个岛之间是否可以拆除
    # 检查第i个岛和第（i
