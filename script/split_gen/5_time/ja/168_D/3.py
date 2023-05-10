def main():
    N, M = map(int, input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    #print(N)
    #print(M)
    #print("-----")
    #グラフ作成
    #隣接リスト作成
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])
    #print(graph)
    #print("-----")
    #BFS
    #初期化
    from collections import deque
    queue = deque()
    queue.append(1)
    visited = [False]*(N+1)
    visited[1] = True
    #print(queue)
    #print(visited)
    #print("-----")
    #探索
    #各部屋からの移動回数を記録
    #部屋1からの移動回数は0
    #各部屋に道しるべを設置する部屋番号を記録
    #部屋1には道しるべを設置しない
    #部屋1の道しるべは、部屋1に設置する
    #道しるべを設置しない場合は-1を記録
    #道しるべの設置は、道しるべを設置する部屋からの移動回数が1増えるごとに行う
    #道しるべを設置する部屋からの移動回数が1増えるごとに、道しるべを設置する部屋からの移動回数を記録する
    #道しるべを設置する部屋からの移動回数が1増えるごとに、道しるべを設置する部屋を記録する
    #道しるべ
