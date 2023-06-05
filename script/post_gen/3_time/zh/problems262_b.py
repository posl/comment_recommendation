Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    pass

=======
Suggestion 2

def readinput():
    n,m=map(int,input().split())
    uv=[]
    for _ in range(m):
        u,v=map(int,input().split())
        uv.append((u,v))
    return n,m,uv

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))

    # print(edges)
    cnt = 0
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            if edges[i][0] in edges[j] and edges[i][1] in edges[j]:
                cnt += 1
                # print(edges[i], edges[j])
    print(int(cnt/3))

solve()

=======
Suggestion 4

def get_input():
    n,m = map(int,input().split())
    u = []
    v = []
    for i in range(m):
        u_i,v_i = map(int,input().split())
        u.append(u_i)
        v.append(v_i)
    return n,m,u,v

=======
Suggestion 5

def get_input():
    line = raw_input()
    line = line.split()
    n = int(line[0])
    m = int(line[1])
    edges = []
    for i in range(m):
        line = raw_input()
        line = line.split()
        edges.append([int(line[0]), int(line[1])])
    return n, m, edges

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int,input().split())))
    print(edges)
    count = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            for k in range(j+1,n+1):
                if [i,j] in edges and [j,k] in edges and [k,i] in edges:
                    count += 1
    print(count)

=======
Suggestion 7

def check(a, b, c):
    if a < b and b < c:
        return True
    else:
        return False

=======
Suggestion 8

def get_edge_num():
    n,m = map(int,raw_input().split())
    edge_list = []
    for i in range(m):
        edge_list.append(map(int,raw_input().split()))
    return n,m,edge_list

=======
Suggestion 9

def main():
    pass
