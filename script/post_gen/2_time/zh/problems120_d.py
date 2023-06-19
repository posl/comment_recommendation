Synthesizing 9/10 solutions

=======
Suggestion 1

def find_parent(x, parents):
    if parents[x] == x:
        return x
    else:
        parents[x] = find_parent(parents[x], parents)
        return parents[x]

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    #print(AB)
    #print(N, M)
    #print(AB)
    #print(AB[0][0])
    #print(AB[0][1])
    #print(AB[1][0])
    #print(AB[1][1])
    #print(AB[2][0])
    #print(AB[2][1])
    #print(AB[3][0])
    #print(AB[3][1])
    #print(AB[4][0])
    #print(AB[4][1])
    #print(AB[5][0])
    #print(AB[5][1])
    #print(AB[6][0])
    #print(AB[6][1])
    #print(AB[7][0])
    #print(AB[7][1])
    #print(AB[8][0])
    #print(AB[8][1])
    #print(AB[9][0])
    #print(AB[9][1])
    #print(AB[10][0])
    #print(AB[10][1])
    #print(AB[11][0])
    #print(AB[11][1])
    #print(AB[12][0])
    #print(AB[12][1])
    #print(AB[13][0])
    #print(AB[13][1])
    #print(AB[14][0])
    #print(AB[14][1])
    #print(AB[15][0])
    #print(AB[15][1])
    #print(AB[16][0])
    #print(AB[16][1])
    #print(AB[17][0])
    #print(AB[17][1])
    #print(AB[18][0])
    #print(AB[18][1])
    #print(AB[19][0])
    #print(AB[19][1])
    #print(AB[20][0])
    #print(AB[20][1])
    #print(AB[21][0])
    #print(AB[21][1])
    #print(AB

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    print(N, M)
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)
    print("hello world")

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a=[]
    b=[]
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    print(a,b)

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    bridge = [0] * N
    bridge[0] = 1
    for i in range(M-1, -1, -1):
        a = A[i] - 1
        b = B[i] - 1
        if bridge[a] == 1 and bridge[b] == 0:
            bridge[b] = 1
    bridge = bridge[::-1]
    # print(bridge)
    for i in range(1, N):
        bridge[i] += bridge[i-1]
    # print(bridge)
    for i in range(M):
        a = A[i] - 1
        b = B[i] - 1
        if bridge[b] - bridge[a] == 0:
            print(bridge[-1] * (bridge[-1]-1) // 2)
        else:
            print(bridge[-1] * (bridge[-1]-1) // 2 - (bridge[b] - bridge[a]) * (bridge[b] - bridge[a] - 1) // 2)


solve()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    bridge = []
    for i in range(m):
        bridge.append(list(map(int, input().split())))

    bridge.sort(key=lambda x: x[1])

    # print(bridge)

    ans = [0 for i in range(m)]
    uf = UnionFind(n)
    for i in range(m):
        ans[i] = uf.size(bridge[i][0] - 1) * uf.size(bridge[i][1] - 1)
        uf.union(bridge[i][0] - 1, bridge[i][1] - 1)

    for i in range(m - 1, 0, -1):
        ans[i - 1] -= ans[i]

    for i in range(m):
        print(ans[i])

=======
Suggestion 7

def findRoot(roots, i):
    if roots[i] == i:
        return i
    else:
        roots[i] = findRoot(roots, roots[i])
        return roots[i]

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    print(N)
    print(M)
    print(A)
    print(B)

=======
Suggestion 9

def findRoot(x):
    global root
    if root[x] == x:
        return x
    else:
        root[x] = findRoot(root[x])
        return root[x]
