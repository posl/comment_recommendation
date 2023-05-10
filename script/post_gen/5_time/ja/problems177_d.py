Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    friends = []
    for i in range(M):
        friends.append(list(map(int, input().split())))
    print(friends)
    #friends = [[1, 2], [3, 4], [5, 1]]
    #friends = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    #friends = [[3, 1], [4, 1], [5, 9], [2, 6]]
    #N = 10
    #M = 4
    friend_group = [[0] * N for i in range(N)]
    for i in range(M):
        friend_group[friends[i][0] - 1][friends[i][1] - 1] = 1
        friend_group[friends[i][1] - 1][friends[i][0] - 1] = 1
    print(friend_group)
    for i in range(N):
        for j in range(N):
            if friend_group[i][j] == 1:
                for k in range(N):
                    if friend_group[j][k] == 1:
                        friend_group[i][k] = 1
                        friend_group[k][i] = 1
    print(friend_group)
    result = 0
    for i in range(N):
        if sum(friend_group[i]) == 0:
            result += 1
    print(result)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    friends = [[] for i in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        friends[a].append(b)
        friends[b].append(a)
    ans = 0
    visited = [False for i in range(n+1)]
    for i in range(1,n+1):
        if visited[i] == False:
            ans += 1
            visited[i] = True
            queue = [i]
            while queue:
                now = queue.pop(0)
                for j in friends[now]:
                    if visited[j] == False:
                        visited[j] = True
                        queue.append(j)
    print(ans)

=======
Suggestion 3

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    p = [i for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        p[a] = min(p[a], p[b])
        p[b] = min(p[a], p[b])
    print(len(set(p)))

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    visited = [False] * n
    ans = 0
    for i in range(n):
        if visited[i]:
            continue
        ans += 1
        visited[i] = True
        stack = [i]
        while stack:
            v = stack.pop()
            for nv in graph[v]:
                if visited[nv]:
                    continue
                visited[nv] = True
                stack.append(nv)
    print(ans)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    friend_list = [list(map(int,input().split())) for _ in range(M)]
    friend_dict = {i:[] for i in range(1,N+1)}
    for a,b in friend_list:
        friend_dict[a].append(b)
        friend_dict[b].append(a)
    group_list = []
    for i in range(1,N+1):
        if i in group_list:
            continue
        group = [i]
        group_list.append(i)
        while len(group) > 0:
            group = list(set(group))
            friend = []
            for j in group:
                friend += friend_dict[j]
            friend = list(set(friend))
            friend = [i for i in friend if i not in group_list]
            group_list += friend
            group = friend
    print(len(group_list))

=======
Suggestion 7

def get_parent(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = get_parent(parents[x])
        return parents[x]

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    ab.sort()
    #print(ab)
    ans = 1
    num = 1
    for i in range(1,m):
        if ab[i-1][0] == ab[i][0]:
            if ab[i-1][1] != ab[i][1]:
                num += 1
                if num > ans:
                    ans = num
            else:
                pass
        else:
            num = 1
    print(ans)

=======
Suggestion 9

def find_root(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_root(par[x])
        return par[x]
