def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = []
    ans.append(N*(N-1)//2)
    uf = UnionFind(N)
    for i in range(M-1, 0, -1):
        a = AB[i][0]-1
        b = AB[i][1]-1
        if uf.same(a, b):
            ans.append(ans[-1])
        else:
            ans.append(ans[-1] - uf.size(a)*uf.size(b))
            uf.union(a, b)
    for i in range(M-1, -1, -1):
        print(ans[i])
