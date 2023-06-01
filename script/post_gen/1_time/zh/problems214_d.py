Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    uf = UnionFind(n)
    ans = 0
    for w, u, v in edges:
        ans += w * uf.size(u) * uf.size(v)
        uf.union(u, v)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    uvw = []
    for i in range(N-1):
        uvw.append(list(map(int, input().split())))
    #print(uvw)
    #uvw = [[1, 2, 10], [2, 3, 20]]
    #uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14]]
    #uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14], [3, 1, 3]]
    #uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14], [3, 1, 3], [5, 6, 4], [5, 7, 6], [7, 8, 10], [7, 9, 8], [9, 10, 7], [8, 11, 9], [9, 12, 12]]
    #uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14], [3, 1, 3], [5, 6, 4], [5, 7, 6], [7, 8, 10], [7, 9, 8], [9, 10, 7], [8, 11, 9], [9, 12, 12], [11, 13, 11], [11, 14, 13], [13, 15, 15], [13, 16, 14], [15, 17, 16], [16, 18, 17]]
    #uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14], [3, 1, 3], [5, 6, 4], [5, 7, 6], [7,

=======
Suggestion 4

def main():
    print("Hello World!")

=======
Suggestion 5

def get_max_weight(x, y, w, s):
    if len(x) == 0:
        return s
    else:
        return get_max_weight(x[1:], y[1:], w[1:], max(s, w[0], get_max_weight(x[1:], y[1:], w[1:], s)))

=======
Suggestion 6

def get_max_weight(edges, u, v):
    if u == v:
        return 0
    else:
        max_weight = 0
        for e in edges:
            if (e[0] == u and e[1] == v) or (e[0] == v and e[1] == u):
                if e[2] > max_weight:
                    max_weight = e[2]
                    break
        for e in edges:
            if e[0] == u:
                weight = get_max_weight(edges, e[1], v)
                if weight > max_weight:
                    max_weight = weight
            elif e[1] == u:
                weight = get_max_weight(edges, e[0], v)
                if weight > max_weight:
                    max_weight = weight
        return max_weight

=======
Suggestion 7

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])
    # print(edges)
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            u, v, w = edges[i]
            if u < v:
                ans += w
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    # 1 <= N <= 10^5
    # 1 <= u_i, v_i <= N
    # 1 <= w_i <= 10^7
    # 给定的图是一棵树。
    # 输入的所有数值都是整数。
    # 输入
    # 输入是由标准输入给出的，格式如下：
    # N
    # u_1 v_1 w_1
    # .
    # .
    # .
    # u_{N - 1} v_{N - 1} w_{N - 1}
    # 3
    # 1 2 10
    # 2 3 20
    # 1 2 1
    # 2 3 2
    # 4 2 5
    # 3 5 14
    # 输出
    # 打印答案。
    # 样品输出1
    # 50
    # 样本输出2
    # 76
    # 样品输出1
    # 50
    # 样本输出2
    # 76
    # 样品输出1
    # 50
    # 样本输出2
    # 76
    # 样品输出1
    # 50
    # 样本输出2
    # 76
    # 样品输出1
    # 50
    # 样本输出2
    # 76
    # 样品输出1
    # 50
    # 样本输出2
    # 76
    # 样品输出1
    # 50
    # 样本输出2
    # 76
    # 样品输出1
    # 50
    # 样本输出2
    # 76
    # 样品输出1
    # 50
    # 样本输出2
    # 76
    # 样品输出1
    # 50
    #
    # 样本输出2
    # 76
    # 样品输出1
    # 50
    #
    # 样本输出2

=======
Suggestion 9

def main():
    N=int(input())
    uvw=[]
    for i in range(N-1):
        uvw.append([int(i) for i in input().split()])
    uvw.sort(key=lambda x:x[2])
    print(uvw)
    for i in range(N-1):
        for j in range(i+1,N):
            print(uvw[i],uvw[j])
            if uvw[i][0] in uvw[j] or uvw[i][1] in uvw[j]:
                print(uvw[i],uvw[j])
                uvw[i][2]=uvw[j][2]
    print(uvw)
    sum=0
    for i in range(N-1):
        sum+=uvw[i][2]
    print(sum)
