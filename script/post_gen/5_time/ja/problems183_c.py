Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(now, visited, dist, K, N):
    if len(visited) == N:
        if dist + T[now][0] == K:
            return 1
        else:
            return 0
    ret = 0
    for i in range(N):
        if i in visited:
            continue
        ret += dfs(i, visited + [i], dist + T[now][i], K, N)
    return ret

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
print(dfs(0, [0], 0, K, N))

=======
Suggestion 2

def main():
    n,k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1,n):
        ans += t[0][i]
    print(ans)
    return

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    T = []
    for i in range(N):
        T.append(list(map(int, input().split())))

    # 都市1を除く
    cities = list(range(2, N+1))

    # 都市1を除く全ての順列を作成
    from itertools import permutations
    perm_cities = list(permutations(cities))

    # 都市1を除く全ての順列について、都市1から出発し、全ての都市を訪問してから都市1に戻るような経路のうち、移動時間の合計がKになるものの数を求める
    ans = 0
    for perm_city in perm_cities:
        # 都市1から出発
        time = 0
        prev_city = 1
        for city in perm_city:
            time += T[prev_city-1][city-1]
            prev_city = city
        # 都市1に戻る
        time += T[prev_city-1][0]
        if time == K:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(1, N):
        ans += dfs(i, 1 << i, 0, T, N, K)
    print(ans)

=======
Suggestion 5

def dfs(v, visited, n, k, t):
    visited[v] = 1
    if sum(visited) == n:
        if k == 0:
            return 1
        else:
            return 0
    ret = 0
    for i in range(n):
        if visited[i] == 0:
            ret += dfs(i, visited, n, k-t[v][i], t)
    visited[v] = 0
    return ret

n, k = map(int, input().split())
t = []
for _ in range(n):
    t.append(list(map(int, input().split())))

visited = [0]*n
print(dfs(0, visited, n, k, t))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, N):
        ans += dfs(i, 1 << i, i, K, T, N)
    print(ans)

=======
Suggestion 7

def main():
    N,K = map(int, input().split())
    T = []
    for i in range(N):
        T.append(list(map(int, input().split())))
    ans = 0
    for i in range(1,N):
        ans += dfs(i, 1<<i, T, K)
    print(ans)

=======
Suggestion 8

def dfs(now, visited, weight):
    if len(visited) == N:
        if weight == K:
            return 1
        else:
            return 0
    else:
        ret = 0
        for i in range(N):
            if i in visited:
                continue
            else:
                visited.add(i)
                ret += dfs(i, visited, weight + T[now][i])
                visited.remove(i)
        return ret

N, K = map(int, input().split())
T = []
for _ in range(N):
    T.append(list(map(int, input().split())))
visited = set()
visited.add(0)
print(dfs(0, visited, 0))

=======
Suggestion 9

def calc(n, k, a, b):
    if n == 0:
        return 1 if k == 0 else 0
    elif k < 0:
        return 0
    else:
        return sum([calc(n-1, k-a[i][j], a, b) for j in range(n)])

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
print(calc(n, k, a, 0))

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1, n):
        ans += dfs(i, 1 << i, i, t, k)
    print(ans)
