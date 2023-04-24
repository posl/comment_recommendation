Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(M):
        for j in range(M):
            if i==j:
                continue
            if (A[i]==A[j] and B[i]==B[j]) or (A[i]==B[j] and B[i]==A[j]):
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N,M = map(int,input().split())
    graph = [[] for i in range(N+1)]
    for i in range(M):
        A,B = map(int,input().split())
        graph[A].append(B)
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i != j:
                visited = [0 for i in range(N+1)]
                visited[i] = 1
                stack = [i]
                while stack:
                    v = stack.pop()
                    if v == j:
                        ans += 1
                        break
                    for nv in graph[v]:
                        if visited[nv] == 0:
                            visited[nv] = 1
                            stack.append(nv)
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N*N)
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort()
    AB = [[0,0]] + AB + [[N+1,N+1]]
    ans = 0
    for i in range(1,M+1):
        if AB[i][0] == AB[i-1][0]:
            if AB[i][1] != AB[i-1][1] + 1:
                ans += (AB[i][1] - AB[i-1][1] - 1) * (AB[i][1] - AB[i-1][1] - 2) // 2
        else:
            ans += (AB[i][1] - 1) * (AB[i][1] - 2) // 2
            ans += (N - AB[i-1][1]) * (N - AB[i-1][1] - 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    ans = 0
    for i in range(N):
        ans += (N - 1) * (N - 2) // 2
        for j in range(M):
            if AB[j][0] == i + 1:
                ans -= 1
            if AB[j][1] == i + 1:
                ans -= 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        ans += N - 1
        for j in range(M):
            if AB[i][0] == AB[j][1]:
                ans -= 1
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    #print(N, M)
    AB = []
    for _ in range(M):
        A, B = map(int, input().split())
        AB.append([A, B])
    #print(AB)
    #print(len(AB))

    #都市の組み合わせを作成する
    city = []
    for i in range(N):
        for j in range(N):
            if i != j:
                city.append([i+1, j+1])
    #print(city)

    #print(len(city))

    #都市の組み合わせをループして、道路が通っているかどうかを判定する
    count = 0
    for i in range(len(city)):
        #print(city[i])
        for j in range(len(AB)):
            #print(AB[j])
            if city[i][0] == AB[j][0] and city[i][1] == AB[j][1]:
                #print("通っている")
                break
            elif j == len(AB)-1:
                #print("通っていない")
                count += 1
    print(count)

=======
Suggestion 7

def main():
    #入力
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    #グラフの構築
    G = [[] for _ in range(N)]
    for a,b in AB:
        G[a-1].append(b-1)
    #全ての都市の組み合わせについて、スタート地点とゴール地点の組として考えられるものの個数をカウント
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if i in G[j]:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    # 都市のリスト
    city = [i for i in range(1,N+1)]
    # 道路のリスト
    road = []
    for i in range(M):
        A, B = map(int, input().split())
        road.append([A,B])
    # 道路のリストを、都市1から都市2への辺のリストに変換
    # road[0][0] = A_i
    # road[0][1] = B_i
    # road[1][0] = A_j
    # road[1][1] = B_j
    # road[2][0] = A_k
    # road[2][1] = B_k
    # road[3][0] = A_l
    # road[3][1] = B_l
    # road[4][0] = A_m
    # road[4][1] = B_m
    # road[5][0] = A_n
    # road[5][1] = B_n
    # road[6][0] = A_o
    # road[6][1] = B_o
    # road[7][0] = A_p
    # road[7][1] = B_p
    # road[8][0] = A_q
    # road[8][1] = B_q
    # road[9][0] = A_r
    # road[9][1] = B_r
    # road[10][0] = A_s
    # road[10][1] = B_s
    # road[11][0] = A_t
    # road[11][1] = B_t
    # road[12][0] = A_u
    # road[12][1] = B_u
    # road[13][0] = A_v
    # road[13][1] = B_v
    # road[14][0] = A_w
    # road[14][1] = B_w
    # road[15][0] = A_x
    # road[15][1] = B_x
    # road[16][

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    # 2次元配列を作る
    road = [[0 for i in range(N)] for j in range(N)]
    # 道路の情報を入れる
    for i in range(M):
        A, B = map(int, input().split())
        road[A-1][B-1] = 1
    # 道路の情報を出力する
    #for i in range(N):
    #    print(road[i])
    # スタート地点とゴール地点の組として考えられるものの数をカウントする
    count = 0
    for i in range(N):
        for j in range(N):
            if road[i][j] == 1:
                count += 1
    print(count)
