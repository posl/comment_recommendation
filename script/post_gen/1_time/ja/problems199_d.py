Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(3 ** N):
        color = [0] * N
        for j in range(N):
            color[j] = i // (3 ** j) % 3
        ok = True
        for j in range(M):
            if color[A[j] - 1] == color[B[j] - 1]:
                ok = False
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0 for i in range(M)]
    B = [0 for i in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    #print("N = ", N)
    #print("M = ", M)
    #print("A = ", A)
    #print("B = ", B)

    if M == 0:
        print(3**N)
        return

    #print("A = ", A)
    #print("B = ", B)
    #print("M = ", M)
    #print("N = ", N)

    #print("A = ", A)
    #print("B = ", B)
    #print("M = ", M)
    #print("N = ", N)

    #print("A = ", A)
    #print("B = ", B)
    #print("M = ", M)
    #print("N = ", N)

    #print("A = ", A)
    #print("B = ", B)
    #print("M = ", M)
    #print("N = ", N)

    #print("A = ", A)
    #print("B = ", B)
    #print("M = ", M)
    #print("N = ", N)

    #print("A = ", A)
    #print("B = ", B)
    #print("M = ", M)
    #print("N = ", N)

    #print("A = ", A)
    #print("B = ", B)
    #print("M = ", M)
    #print("N = ", N)

    #print("A = ", A)
    #print("B = ", B)
    #print("M = ", M)
    #print("N = ", N)

    #print("A = ", A)
    #print("B = ", B)
    #print("M = ", M)
    #print("N = ", N)

    #print("A = ", A)
    #print("B = ", B)
    #print("M = ", M)
    #print("N = ", N)

    #print("A = ", A)
    #print("B = ", B)
    #print("M = ", M)
    #

=======
Suggestion 3

def main():
    #入力
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)
    #問題の解答
    ans = 3**N
    for i in range(M):
        if A[i] == B[i]:
            ans -= 3**(N - 1)
    #出力
    print(ans)

=======
Suggestion 4

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    N,M = map(int,readline().split())
    if M == 0:
        print(3**N)
    else:
        AB = [list(map(int,readline().split())) for _ in range(M)]
        ab = set()
        for a,b in AB:
            ab.add((a,b))
            ab.add((b,a))
        #print(ab)
        ans = 0
        for i in range(3**N):
            color = []
            for j in range(N):
                color.append(i//(3**j)%3)
            #print(color)
            #print(i)
            flag = True
            for a,b in ab:
                if color[a-1] == color[b-1]:
                    flag = False
                    break
            if flag:
                ans += 1
        print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    if m == 0:
        print(3**n)
        return
    edge = []
    for _ in range(m):
        a, b = map(int, input().split())
        edge.append([a, b])
    ans = 0
    for i in range(3**n):
        color = []
        for j in range(n):
            color.append(i // 3**j % 3)
        ok = True
        for j in range(m):
            if color[edge[j][0] - 1] == color[edge[j][1] - 1]:
                ok = False
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    edge = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        a,b = map(int, input().split())
        edge[a-1][b-1] = 1
        edge[b-1][a-1] = 1
    #print(edge)
    color = [0 for i in range(n)]
    for i in range(n):
        color[i] = 3
    #print(color)
    ans = 0
    for i in range(3**n):
        tmp = i
        for j in range(n):
            color[j] = tmp % 3
            tmp //= 3
        #print(color)
        flag = 0
        for j in range(n):
            for k in range(j + 1, n):
                if edge[j][k] == 1 and color[j] == color[k]:
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        a, b = map(int, input().split())
        AB.append([a, b])
    
    ans = 0
    for i in range(3 ** N):
        tmp = i
        color = []
        for j in range(N):
            color.append(tmp % 3)
            tmp //= 3
        
        flag = 0
        for j in range(M):
            if color[AB[j][0] - 1] == color[AB[j][1] - 1]:
                flag = 1
        
        if flag == 0:
            ans += 1
    
    print(ans)

=======
Suggestion 8

def dfs(v, c):
    global ans
    if v == n:
        ans += 1
        return
    for i in range(3):
        if c[v][i] == 0:
            for j in g[v]:
                c[j][i] += 1
            dfs(v + 1, c)
            for j in g[v]:
                c[j][i] -= 1

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
ans = 0
c = [[0] * 3 for i in range(n)]
dfs(0, c)
print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print("")

    #グラフの初期化
    graph = [[0]*N for i in range(N)]
    #print(graph)
    #print("")

    #グラフの作成
    for i in range(M):
        A_i, B_i = map(int, input().split())
        #print(A_i, B_i)
        graph[A_i-1][B_i-1] = 1
        graph[B_i-1][A_i-1] = 1
        #print(graph)
        #print("")

    #print(graph)
    #print("")

    #print(N, M)
    #print(graph)

    #print("")

    #頂点の色を決める
    color = [0]*N
    #print(color)

    #頂点の色を決める
    def dfs(v):
        #print("v", v)
        #print("color", color)
        #print("")

        #頂点の色を決める
        for c in range(3):
            #print("c", c)
            #print("")

            #頂点の色を決める
            color[v] = c

            #頂点の色を決める
            for i in range(N):
                #print("i", i)
                #print("")

                #頂点の色を決める
                if graph[v][i] == 1 and color[v] == color[i]:
                    #print("graph[v][i]", graph[v][i])
                    #print("color[v]", color[v])
                    #print("color[i]", color[i])
                    #print("")

                    #頂点の色を決める
                    return 0

            #頂点の色を決める
            if v+1 < N:
                #print("v+1", v+1)
                #print("")

                #頂点の色を決める
                if dfs(v+1) == 0:
                    #print("dfs(v+1)", dfs(v+1))
                    #print("")
                    #頂点の色を決める

=======
Suggestion 10

def main():
    #入力
    N, M = map(int, input().split())
    #フラグ
    flag = 0
    #グラフの辺を格納するリスト
    graph = []
    #グラフの辺を格納
    for i in range(M):
        a, b = map(int, input().split())
        graph.append([a, b])
    #グラフの辺を格納したリストの要素数分ループ
    for i in range(M):
        if graph[i][0] == graph[i][1]:
            flag = 1
            break
    #グラフの辺を格納したリストの要素数分ループ
    for i in range(M):
        #グラフの辺を格納したリストの要素数分ループ
        for j in range(M):
            if graph[i][0] == graph[j][0] and graph[i][1] == graph[j][1]:
                flag = 1
                break
    #フラグが立っている場合
    if flag == 1:
        print(0)
    #フラグが立っていない場合
    else:
        print(3 ** N - 2 ** M)
