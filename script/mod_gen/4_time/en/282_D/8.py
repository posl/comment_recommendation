def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[1])
parent = [i for i in range(N+1)]
ans = 0
for u, v in edges:
    if find_parent(parent, u) != find_parent(parent, v):
        ans += 1
        parent[find_parent(parent, u)] = find_parent(parent, v)
print(ans)

if __name__ == '__main__':
    find_parent()