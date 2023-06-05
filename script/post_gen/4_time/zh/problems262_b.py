Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n, m = map(int, input().split(' '))
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n))
    #print(ty

=======
Suggestion 2

def get_num_of_triangle(n, m, e):
    answer = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if e[i][j] == 1:
                for k in range(j+1, n+1):
                    if e[j][k] == 1 and e[i][k] == 1:
                        answer += 1
    return answer

=======
Suggestion 3

def test():
    n,m = 5,6
    edges = [(1,5),(4,5),(2,3),(1,4),(3,5),(2,5)]
    edges = [(1,7),(5,7),(2,5),(3,6),(4,7),(1,5),(2,4),(1,3),(1,6),(2,7)]
    n,m = 3,1
    edges = [(1,2)]
    return n,m,edges

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1][v-1] = 1
        graph[v-1][u-1] = 1
    ans = 0
    for a in range(N):
        for b in range(a+1, N):
            if graph[a][b] != 1:
                continue
            for c in range(b+1, N):
                if graph[b][c] == 1 and graph[c][a] == 1:
                    ans += 1
    print(ans)

=======
Suggestion 5

def get_input():
    line = input()
    n, m = line.split()
    n = int(n)
    m = int(m)
    edges = []
    for i in range(m):
        line = input()
        u, v = line.split()
        u = int(u)
        v = int(v)
        edges.append((u, v))
    return n, m, edges

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    edge = []
    for i in range(m):
        u, v = map(int, input().split())
        edge.append((u, v))
    ans = 0
    for i in range(m):
        u, v = edge[i]
        for j in range(i + 1, m):
            if edge[j][0] == u or edge[j][0] == v or edge[j][1] == u or edge[j][1] == v:
                continue
            ans += 1
    print(ans)

=======
Suggestion 8

def get_num(n, m, uv):
    num = 0
    for i in range(n):
        for j in range(i+1, n):
            if (i+1, j+1) in uv:
                for k in range(j+1, n):
                    if (j+1, k+1) in uv and (i+1, k+1) in uv:
                        num += 1
    return num

=======
Suggestion 9

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

=======
Suggestion 10

def judge(a,b,c):
    if a<b and b<c and a<c:
        return True
    else:
        return False
