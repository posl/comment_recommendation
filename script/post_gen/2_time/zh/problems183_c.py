Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def get_time(n, k, T):
    count = 0
    for i in range(n):
        if T[0][i] == 0:
            continue
        else:
            count += T[0][i] + get_time_helper(n, k, T, i, 1, [0, i])
    return count

=======
Suggestion 3

def dfs(city, time, visited, K):
    global ans
    if len(visited) == N:
        if time + T[city][0] == K:
            ans += 1
        return
    for i in range(N):
        if i not in visited:
            visited.add(i)
            dfs(i, time + T[city][i], visited, K)
            visited.remove(i)
    return

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = set()
visited.add(0)
dfs(0, 0, visited, K)
print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]

    def dfs(city, visited, time):
        if visited == (1 << n) - 1:
            return time + t[city][0] == k
        else:
            return sum(dfs(i, visited | (1 << i), time + t[city][i]) for i in range(n) if not visited >> i & 1)

    print(dfs(0, 1, 0))

=======
Suggestion 5

def get_data():
    n, k = map(int, input().split())
    time = []
    for i in range(n):
        time.append(list(map(int, input().split())))
    return n, k, time

=======
Suggestion 6

def solve():
    return 0

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1, n):
        ans += t[0][i]
    print(ans)

=======
Suggestion 8

def dfs(i, k, n, t, visited):
    if k == 0 and visited == (1 << n) - 1:
        return 1
    ans = 0
    for j in range(n):
        if visited & (1 << j) == 0:
            ans += dfs(j, k - t[i][j], n, t, visited | (1 << j))
    return ans

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
print(dfs(0, k, n, t, 1))
