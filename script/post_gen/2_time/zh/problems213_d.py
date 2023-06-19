Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    roads = []
    for i in range(N-1):
        roads.append(list(map(int, input().split())))
    print(roads)
    #print(N)
    #print(N)
    #print(N)

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N-1):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    for i in range(N-1):
        print(A[i],B[i])
    print(N)

=======
Suggestion 3

def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    AB.sort()
    ans = [1]
    for i in range(N-1):
        a, b = AB[i]
        if a == ans[-1]:
            ans.append(b)
        elif b == ans[-1]:
            ans.append(a)
    print(*ans)

solve()

=======
Suggestion 4

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    graph = [[] for _ in range(n+1)]
    for a, b in ab:
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n+1)
    visited[1] = True
    ans = []
    ans.append(1)
    #print(graph)
    #print(visited)
    #print(ans)
    while True:
        for i in graph[ans[-1]]:
            if visited[i] == False:
                visited[i] = True
                ans.append(i)
                break
        else:
            if ans[-1] == 1:
                break
            else:
                ans.pop(-1)
    print(*ans)

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    N = int(input())
    path = [list(map(int, input().split())) for i in range(N-1)]
    print(path)
    print(N)

=======
Suggestion 7

def f():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())

    # print(A)
    # print(B)
    # print(N)

    # 1. 从1开始，找到与1相连的点，记录下来，如果有多个，记录最小的那个
    # 2. 如果有多个，记录最小的那个
    # 3. 如果有多个，记录最小的那个
    # 4. 如果有多个，记录最小的那个
    # 5. 如果有多个，记录最小的那个
    # 6. 如果有多个，记录最小的那个
    # 7. 如果有多个，记录最小的那个
    # 8. 如果有多个，记录最小的那个
    # 9. 如果有多个，记录最小的那个
    # 10. 如果有多个，记录最小的那个
    # 11. 如果有多个，记录最小的那个
    # 12. 如果有多个，记录最小的那个
    # 13. 如果有多个，记录最小的那个
    # 14. 如果有多个，记录最小的那个
    # 15. 如果有多个，记录最小的那个
    # 16. 如果有多个，记录最小的那个
    # 17. 如果有多个，记录最小的那个
    # 18. 如果有多个，记录最小的那个
    # 19. 如果有多个，记录最小的那个
    # 20. 如果有多个，记录最小的那个
    # 21. 如果有多个，记录最小的那个
    # 22. 如果有多个，记录最小的那个
    # 23. 如果有多个，记录最小的

=======
Suggestion 8

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    AB.sort(key=lambda x:x[1])
    AB.sort(key=lambda x:x[0])
    print(AB)
    #for i in range(N-1):
    #    if AB[i][0] == 1:
    #        print(AB[i][0], AB[i][1], end=' ')
    #    else:
    #        print(AB[i][1], end=' ')
    #if AB[N-2][1] != 1:
    #    print(1)

=======
Suggestion 9

def dfs(v, visited, graph, ans):
    visited[v] = True
    ans.append(v)
    for i in range(len(graph[v])):
        if not visited[graph[v][i]]:
            dfs(graph[v][i], visited, graph, ans)
            ans.append(v)

n = int(input())
graph = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
for i in range(n):
    graph[i].sort()
visited = [False] * n
ans = []
dfs(0, visited, graph, ans)
print(*[i+1 for i in ans])

=======
Suggestion 10

def dfs(x):
    global ans
    ans.append(x)
    visited[x] = True
    for i in range(len(g[x])):
        if not visited[g[x][i]]:
            dfs(g[x][i])
            ans.append(x)
    return

n = int(input())
g = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(1,n+1):
    g[i].sort()
visited = [False] * (n+1)
ans = []
dfs(1)
print(*ans)
