Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    pass

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    N = int(input())
    u = [0] * (N - 1)
    v = [0] * (N - 1)
    w = [0] * (N - 1)
    for i in range(N - 1):
        u[i], v[i], w[i] = map(int, input().split())
    print(solve(N, u, v, w))

=======
Suggestion 4

def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N - 1)]
    data.sort(key=lambda x: x[2])
    # print(data)
    # print(N)
    # print(data)
    # print(data[0][1])
    # print(data[0][2])
    # print(data[0][0])
    # print(data[1][1])
    # print(data[1][2])
    # print(data[1][0])
    # print(data[2][1])
    # print(data[2][2])
    # print(data[2][0])
    # print(data[3][1])
    # print(data[3][2])
    # print(data[3][0])
    # print(data[4][1])
    # print(data[4][2])
    # print(data[4][0])
    # print(data[5][1])
    # print(data[5][2])
    # print(data[5][0])
    # print(data[6][1])
    # print(data[6][2])
    # print(data[6][0])
    # print(data[7][1])
    # print(data[7][2])
    # print(data[7][0])
    # print(data[8][1])
    # print(data[8][2])
    # print(data[8][0])
    # print(data[9][1])
    # print(data[9][2])
    # print(data[9][0])
    # print(data[10][1])
    # print(data[10][2])
    # print(data[10][0])
    # print(data[11][1])
    # print(data[11][2])
    # print(data[11][0])
    # print(data[12][1])
    # print(data[12][2])
    # print(data[12][0])
    # print(data[13][1])
    # print(data[13][2])
    # print(data[13][0])
    # print(data[14][1])
    # print(data[14][2])
    # print(data[14][0])
    # print(data[15][1])
    # print(data[15][2])
    # print(data[15][0])
    # print(data[16][1])
    # print(data

=======
Suggestion 5

def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u,v,w = map(int,input().split())
        edges.append((w,u,v))
    edges.sort()
    uf = UnionFind(n)
    ans = 0
    for w,u,v in edges:
        ans += w * uf.size(u) * uf.size(v)
        uf.union(u,v)
    print(ans)

=======
Suggestion 6

def solve():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    edges.sort(key=lambda x: x[2], reverse=True)

    parents = [i for i in range(n+1)]
    ranks = [0 for i in range(n+1)]

    def find(x):
        if parents[x] == x:
            return x
        else:
            return find(parents[x])

    def union(x, y):
        x_root = find(x)
        y_root = find(y)

        if x_root == y_root:
            return False

        if ranks[x_root] > ranks[y_root]:
            parents[y_root] = x_root
        elif ranks[y_root] > ranks[x_root]:
            parents[x_root] = y_root
        else:
            parents[y_root] = x_root
            ranks[x_root] += 1
        return True

    def same(x, y):
        return find(x) == find(y)

    num = [1 for i in range(n+1)]
    res = 0
    for u, v, w in edges:
        res += w * num[find(u)] * num[find(v)]
        union(u, v)
        num[find(u)] += num[find(v)]
    print(res)
