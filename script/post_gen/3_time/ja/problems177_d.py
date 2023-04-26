Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 2

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 3

def find_root(x):
    if root[x] == x:
        return x
    else:
        root[x] = find_root(root[x])
        return root[x]

=======
Suggestion 4

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

seen = [False] * N

ans = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(v)
    ans += 1

print(ans)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = [0] * (n+1)
    for i in range(m):
        x,y = map(int,input().split())
        a[x] += 1
        a[y] += 1
    for i in range(1,n+1):
        if a[i] % 2 != 0:
            print("NO")
            return
    print("YES")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    friends = [list(map(int, input().split())) for _ in range(M)]
    friend_list = [[] for _ in range(N)]
    for i in range(M):
        friend_list[friends[i][0]-1].append(friends[i][1]-1)
        friend_list[friends[i][1]-1].append(friends[i][0]-1)
    #print(friend_list)
    group = 0
    for i in range(N):
        if friend_list[i] == []:
            group += 1
            continue
        if i in friend_list[i]:
            group += 1
            continue
        for j in friend_list[i]:
            if j in friend_list[j]:
                group += 1
                break
    print(group)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    ab = sorted(ab, key=lambda x: x[0])
    ab = sorted(ab, key=lambda x: x[1])
    #print(ab)

    # 隣り合う要素が同じ値であるかどうかを確認する
    # 隣り合う要素が同じ値である場合、グループ数を1つ減らす
    cnt = 0
    for i in range(1,m):
        if ab[i-1][1] == ab[i][1]:
            cnt += 1
    #print(cnt)

    # グループ数は、m-1からcntを引いた値
    print(m-1-cnt)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #
