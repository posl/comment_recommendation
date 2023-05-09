Synthesizing 10/10 solutions

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

def find_parent(parent, i):
    if parent[i] == -1:
        return i
    if parent[i] != -1:
        return find_parent(parent, parent[i])

=======
Suggestion 3

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    friend_list = [set() for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        friend_list[a-1].add(b-1)
        friend_list[b-1].add(a-1)
    ans = 0
    for i in range(N):
        if len(friend_list[i]) == 0:
            ans += 1
            continue
        friend_list[i].add(i)
        tmp = {i}
        while len(tmp) > 0:
            tmp2 = set()
            for j in tmp:
                tmp2 = tmp2 | friend_list[j]
            tmp = tmp2 - friend_list[i]
            friend_list[i] = friend_list[i] | tmp2
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    print(N)

=======
Suggestion 6

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        if root_x > root_y:
            parent[root_x] += parent[root_y]
            parent[root_y] = root_x
        else:
            parent[root_y] += parent[root_x]
            parent[root_x] = root_y

=======
Suggestion 7

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    friends = []
    for _ in range(M):
        A, B = map(int, input().split())
        friends.append([A, B])

    print(len(set([i for i in range(1, N+1)]) - set([i for i, j in friends if i in j or j in i])))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[0])
    group = [1] * N
    for i in range(M):
        if group[AB[i][0] - 1] == 1:
            group[AB[i][0] - 1] = group[AB[i][1] - 1]
        elif group[AB[i][1] - 1] == 1:
            group[AB[i][1] - 1] = group[AB[i][0] - 1]
        else:
            group[AB[i][1] - 1] = group[AB[i][0] - 1]
    print(len(set(group)))

=======
Suggestion 10

def find_set(x):
    if x != par[x]:
        par[x] = find_set(par[x])
    return par[x]
