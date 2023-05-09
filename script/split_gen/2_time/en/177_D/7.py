def main():
    n,m = map(int,input().split())
    uf = UnionFind(n)
    for _ in range(m):
        a,b = map(int,input().split())
        uf.union(a-1,b-1)
    print(uf.group_num-1)
