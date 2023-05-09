def main():
    n = int(input())
    e = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        e[u-1].append((v-1, w))
        e[v-1].append((u-1, w))
    def dfs(s):
        q = [s]
        d = [-1]*n
        d[s] = 0
        while q:
            u = q.pop()
            for v, w in e[u]:
                if d[v] == -1:
                    d[v] = d[u] + w
                    q.append(v)
        return d
    d1 = dfs(0)
    d2 = dfs(d1.index(max(d1)))
    print(sum(d2))
