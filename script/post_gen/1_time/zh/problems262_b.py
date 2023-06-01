Synthesizing 10/10 solutions

=======
Suggestion 1

def problem262_b():
    pass

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    U = [0] * M
    V = [0] * M
    for i in range(M):
        U[i], V[i] = map(int, input().split())
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            u1 = U[i]
            v1 = V[i]
            u2 = U[j]
            v2 = V[j]
            if u1 == u2 or u1 == v2 or v1 == u2 or v1 == v2:
                continue
            if (u1 == v1 and u2 == v2) or (u1 == v2 and u2 == v1):
                continue
            if (u1 == u2 and v1 == v2):
                continue
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def countTriangle(graph):
    count = 0
    for i in range(1, len(graph) + 1):
        for j in range(i + 1, len(graph) + 1):
            if graph[i][j] == 1:
                for k in range(j + 1, len(graph) + 1):
                    if graph[i][k] == 1 and graph[j][k] == 1:
                        count += 1
    return count

=======
Suggestion 5

def get_input():
    input_list = []
    while True:
        try:
            input_list.append(raw_input())
        except EOFError:
            break
    return input_list

=======
Suggestion 6

def check(a, b, c, edges):
    if (a, b) in edges and (b, c) in edges and (c, a) in edges:
        return True
    else:
        return False

=======
Suggestion 7

def solve():
    pass

=======
Suggestion 8

def find(a,b,c):
    if a>b:
        a,b=b,a
    if b>c:
        b,c=c,b
    if a>b:
        a,b=b,a
    return a,b,c

=======
Suggestion 9

def main():
    N = 5
    M = 6
    U = [1,4,2,1,3,2]
    V = [5,5,3,4,5,5]
    #print(N, M)
    #print(U)
    #print(V)
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            if U[i] == U[j] or U[i] == V[j] or V[i] == U[j] or V[i] == V[j]:
                continue
            if (U[i], V[i]) == (U[j], V[j]) or (U[i], V[i]) == (V[j], U[j]) or (V[i], U[i]) == (U[j], V[j]) or (V[i], U[i]) == (V[j], U[j]):
                continue
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    edge = []
    for i in range(M):
        edge.append(list(map(int, input().split())))
    edge.sort(key=lambda x: x[0])
    # print(edge)
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            if edge[i][0] == edge[j][0]:
                continue
            for k in range(j + 1, M):
                if edge[j][0] == edge[k][0]:
                    continue
                if edge[i][0] == edge[k][0]:
                    continue
                if edge[i][1] == edge[j][1] and edge[j][1] == edge[k][1]:
                    ans += 1
    print(ans)
