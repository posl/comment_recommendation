Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    print(n,m,ab)

=======
Suggestion 2

def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    return True

N, M = map(int, input().split())
G = [[] for _ in range(N)]
color = [0] * N

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = 1
for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            ans = 0
            break
    ans *= 3

print(ans)

=======
Suggestion 3

def main():
    print('Hello World')

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    print(N, M, AB)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        edges.append(list(map(int, input().split())))
    print(edges)

=======
Suggestion 6

def dfs(v, c):
    color[v] = c
    for i in range(len(graph[v])):
        if color[graph[v][i]] == c:
            return False
        if color[graph[v][i]] == 0 and not dfs(graph[v][i], -c):
            return False
    return True

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
color = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            r = color.count(1)
            b = color.count(-1)
            ans += r * (r - 1) // 2 + b * (b - 1) // 2
        else:
            ans = 0
            break
print(ans)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    if M == 0:
        print(3**N)
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    # print(AB)
    # print(N, M)
    # print(3**N)
    ans = 0
    for i in range(3**N):
        # print(i)
        flag = True
        for j in range(N):
            for k in range(j+1, N):
                # print(j, k)
                if i//(3**j)%3 == i//(3**k)%3:
                    for l in range(M):
                        if AB[l][0] == j+1 and AB[l][1] == k+1:
                            flag = False
                            break
                        if AB[l][0] == k+1 and AB[l][1] == j+1:
                            flag = False
                            break
        if flag:
            ans += 1
    print(ans)
    # print(3**N)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    print(n, m)
    print(edges)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    #print(N, M)
    #print(AB)
    #print(len(AB))
    #print(len(AB[0]))

    # 頂点の色の組み合わせを全探索
    # 赤:0, 緑:1, 青:2
    # 赤:1, 緑:2, 青:0
    # 赤:2, 緑:0, 青:1
    # 3通り
    # 赤:0, 緑:2, 青:1
    # 赤:1, 緑:0, 青:2
    # 赤:2, 緑:1, 青:0
    # 3通り
    # 3^N通り
    ans = 0
    for i in range(3**N):
        #print(i)
        #print(i//3**0%3, i//3**1%3, i//3**2%3, i//3**3%3, i//3**4%3, i//3**5%3, i//3**6%3, i//3**7%3, i//3**8%3, i//3**9%3)
        #print(i//3**0%3, i//3**1%3, i//3**2%3, i//3**3%3, i//3**4%3, i//3**5%3, i//3**6%3, i//3**7%3, i//3**8%3, i//3**9%3)
        #print(i//3**0%3, i//3**1%3, i//3**2%3, i//3**3%3, i//3**4%3, i//3**5%3, i//3**6%3, i//3**7%3, i//3**8%3, i//3**9%3)
        #print(i//

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N, M, A, B)
