def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    uf = UnionFind(N)
    ans = [0]
    for a, b in AB:
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans.append(ans[-1])
        else:
            ans.append(ans[-1] + uf.size(a) * uf.size(b))
            uf.union(a, b)
    ans.pop(0)
    ans.reverse()
    print(*ans, sep='\n')
