def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    #print(N)
    #print(A)
    #print(B)
    #道路と都市の関係をグラフで表す
    graph = [[] for _ in range(N)]
    for i in range(N-1):
        graph[A[i]-1].append(B[i]-1)
        graph[B[i]-1].append(A[i]-1)
    #print(graph)
    #旅のルートを記録
    route = [0]
    #訪れた都市を記録
    visited = [0] * N
    #現在いる都市を記録
    now = 0
    #訪れた都市を記録
    visited[now] = 1
    #print(visited)
    #print(route)
    #都市1に戻ってきたら終了
    while now != 0:
        #print("now = ", now)
        #print("route = ", route)
        #print("visited = ", visited)
        #print("graph[now] = ", graph[now])
        #print("visited[graph[now][i]] = ", visited[graph[now][i]])
        #print("visited[graph[now][i]] = ", visited[graph[now][i]])
        #print("route[-1] = ", route[-1])
        #print("graph[route[-1]] = ", graph[route[-1]])
        #print("now = ", now)
        #print("graph[route[-1]] = ", graph[route[-1]])
        #print("visited[graph[route[-1]][i]] = ", visited[graph[route[-1]][i]])
        #print("visited[graph[route[-1]][i]] = ", visited[graph[route[-1]][i]])
        #次にいく都市があれば、次にいく都市へ移動
        #都市1に戻ってきたら終了
        #次にい
