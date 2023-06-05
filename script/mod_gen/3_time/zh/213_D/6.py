def dfs(u, p):
    global time
    time += 1
    first[u] = time
    for v in G[u]:
        if v == p:
            continue
        dfs(v, u)
    time += 1
    last[u] = time
N = int(input())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
first = [0] * N
last = [0] * N
time = 0
dfs(0, -1)
ans = []
for i in range(N):
    ans.append((first[i], i + 1))
ans.sort()
for i in range(N):
    ans.append((last[i], -(i + 1)))
ans.sort()
for i in range(2 * N):
    print(ans[i][1], end = ' ')
print()

if __name__ == '__main__':
    dfs()