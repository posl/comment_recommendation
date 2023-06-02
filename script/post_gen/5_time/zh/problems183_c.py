Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, N):
        ans += dfs(i, 1 << i, i, N, K, T)
    print(ans)

=======
Suggestion 2

def all_path(n):
    all_path = []
    for i in range(1,n):
        for j in range(i+1,n+1):
            path = [i,j]
            all_path.append(path)
    return all_path

=======
Suggestion 3

def solve():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(1, n):
        cnt += i * (n - i)
    for i in range(1, 1 << n):
        for j in range(1, 1 << n):
            if i & j == 0:
                continue
            s = 0
            for a in range(n):
                for b in range(n):
                    if (i >> a) & 1 and (j >> b) & 1:
                        s += t[a][b]
            if s == k:
                cnt -= 1
    print(cnt)

solve()

=======
Suggestion 4

def get_time(i, j, N, T, K, path, visited, sum, count):
    if i == 0 and j == 0 and sum == K and count == N:
        return 1
    else:
        res = 0
        for k in range(N):
            if visited[k] == 0:
                visited[k] = 1
                path.append(k)
                res += get_time(j, k, N, T, K, path, visited, sum + T[j][k], count + 1)
                path.pop()
                visited[k] = 0
        return res

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def get_input():
    line1 = input().split()
    n = int(line1[0])
    k = int(line1[1])
    T = []
    for i in range(n):
        line = input().split()
        T.append([int(i) for i in line])
    return n, k, T

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(1, n):
        ans += t[0][i]
    if k == ans:
        print(1)
        return

    import itertools
    for v in itertools.permutations(range(1, n)):
        now = 0
        for i in range(n - 2):
            now += t[v[i]][v[i + 1]]
        now += t[v[-1]][0]
        if now == k:
            ans += 1

    print(ans)

=======
Suggestion 8

def read_data():
    N, K = map(int, input().split())
    T = []
    for _ in range(N):
        T.append(list(map(int, input().split())))
    return N, K, T

N, K, T = read_data()
