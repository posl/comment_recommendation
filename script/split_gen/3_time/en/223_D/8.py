def find_smallest_permutation(n, m, a, b):
    ans = []
    g = [[] for _ in range(n)]
    for i in range(m):
        g[a[i]-1].append(b[i]-1)
        g[b[i]-1].append(a[i]-1)
    used = [False] * n
    for i in range(n):
        if not used[i]:
            used[i] = True
            que = [i]
            while que:
                v = que.pop()
                ans.append(v+1)
                for to in g[v]:
                    if not used[to]:
                        used[to] = True
                        que.append(to)
    if len(ans) != n:
        return -1
    else:
        return ans
n, m = map(int, input().split())
a = []
b = []
for i in range(m):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)
ans = find_smallest_permutation(n, m, a, b)
