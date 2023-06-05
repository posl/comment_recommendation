def dfs(now, pre):
    for i in range(len(tree[now])):
        if tree[now][i] == pre: continue
        dfs(tree[now][i], now)
        cnt[now] += cnt[tree[now][i]]
N, Q = map(int, input().split())
tree = [[] for _ in range(N)]
cnt = [0 for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
for _ in range(Q):
    p, x = map(int, input().split())
    cnt[p - 1] += x
dfs(0, -1)
print(' '.join(map(str, cnt)))

if __name__ == '__main__':
    dfs()