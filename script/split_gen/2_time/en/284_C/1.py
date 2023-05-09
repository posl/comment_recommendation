def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for _ in range(M):
        a, b = map(int, input().split())
        uf.union(a-1, b-1)
    print(uf.group_count())
