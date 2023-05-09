Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1, n):
        ans += dfs(i, 1 << i, t, k, 0)
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1, n):
        ans += dfs(i, 1 << i, k - t[0][i], n, t)
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(1, n):
        cnt += dfs(i, 1 << i, n, k, t)
    return cnt

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    T = []
    for _ in range(N):
        T.append(list(map(int, input().split())))

    from itertools import permutations
    ans = 0
    for p in permutations(range(1, N)):
        time = 0
        cur = 0
        for i in p:
            time += T[cur][i]
            cur = i
        time += T[cur][0]
        if time == K:
            ans += 1

    print(ans)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for perm in itertools.permutations(range(1, N)):
        time = 0
        now = 0
        for next in perm:
            time += T[now][next]
            now = next
        time += T[now][0]
        if time == K:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]

    def dfs(cur, visited, cost):
        if len(visited) == N:
            if cost + T[cur][0] == K:
                return 1
            else:
                return 0

        res = 0
        for i in range(N):
            if i not in visited:
                res += dfs(i, visited + [i], cost + T[cur][i])
        return res

    print(dfs(0, [0], 0))

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    #print(N, K, T)
    cnt = 0
    for i in range(1, N):
        cnt += dfs(i, N, K, T, 0)
    print(cnt)

=======
Suggestion 8

def path183_c():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1, n):
        ans += dfs(i, [i], t, k)
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    print(dfs(T, N, K))

=======
Suggestion 10

def get_paths(start, cities, visited, total, k):
    if len(visited) == len(cities):
        if start in cities:
            total += cities[start]
            if total == k:
                return 1
            else:
                return 0
    else:
        total += cities[start]
        visited.append(start)
        for city in cities:
            if city not in visited:
                return get_paths(city, cities, visited, total, k)
    return 0
