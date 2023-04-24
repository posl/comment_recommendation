Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    next = [i + 1 for i in range(N)]
    prev = [i - 1 for i in range(N)]
    for _ in range(Q):
        c, x, y = map(int, input().split())
        if c == 1:
            prev[next[x - 1]] = y - 1
            next[prev[y - 1]] = x - 1
            prev[x - 1] = y - 1
            next[y - 1] = x - 1
        elif c == 2:
            prev[next[x - 1]] = prev[y - 1]
            next[prev[y - 1]] = next[x - 1]
            prev[x - 1] = x - 1
            next[y - 1] = y - 1
        else:
            ans = []
            while x > 0:
                ans.append(x)
                x = next[x - 1] + 1
            print(len(ans), *ans)

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    par = [-1] * (N + 1)
    rank = [0] * (N + 1)
    for _ in range(Q):
        query = list(map(int, input().split()))
        c = query[0]
        if c == 1:
            x, y = query[1], query[2]
            unite(x, y, par, rank)
        elif c == 2:
            x, y = query[1], query[2]
            if same(x, y, par):
                unite(x, y, par, rank)
        else:
            x = query[1]
            ans = []
            for i in range(1, N + 1):
                if same(x, i, par):
                    ans.append(i)
            print(len(ans), *ans)

=======
Suggestion 3

def main():
    N,Q = map(int,input().split())
    train = [0] * (N+1)
    for i in range(1,N+1):
        train[i] = i
    for i in range(Q):
        c,x,y = map(int,input().split())
        if c == 1:
            train[x] = y
        elif c == 2:
            train[x] = x
        else:
            ans = [x]
            while train[x] != x:
                x = train[x]
                ans.append(x)
            print(len(ans),*ans)

=======
Suggestion 4

def main():
    n,q=map(int,input().split())
    trains=[i for i in range(n+1)]
    for i in range(q):
        query=list(map(int,input().split()))
        if query[0]==1:
            trains[query[2]]=trains[query[1]]
        elif query[0]==2:
            trains[query[2]]=query[2]
        else:
            ans=[]
            for j in range(1,n+1):
                if trains[j]==query[1]:
                    ans.append(j)
            print(len(ans),*ans)
    
    return 0

=======
Suggestion 5

def main():
    N, Q = [int(i) for i in input().split()]
    trains = [i for i in range(N)]
    for _ in range(Q):
        q = [int(i) for i in input().split()]
        if q[0] == 1:
            trains[q[1]-1] = q[2]-1
        elif q[0] == 2:
            trains[q[1]-1] = q[1]-1
        else:
            train = trains[q[1]-1]
            ans = [q[1]]
            while train != q[1]-1:
                ans.append(train+1)
                train = trains[train]
            print(len(ans),*ans)

=======
Suggestion 6

def main():
    N,Q = map(int,input().split())
    parent = [-1] * (N+1)
    rank = [0] * (N+1)
    for i in range(Q):
        q = list(map(int,input().split()))
        if q[0] == 1:
            unite(q[1],q[2],parent,rank)
        elif q[0] == 2:
            root1 = find(q[1],parent)
            root2 = find(q[2],parent)
            if root1 != root2:
                if rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    if rank[root1] == rank[root2]:
                        rank[root1] += 1
        else:
            ans = []
            for j in range(1,N+1):
                if find(j,parent) == find(q[1],parent):
                    ans.append(j)
            print(len(ans),*ans)

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    # 電車の番号を格納するリスト
    trains = [i for i in range(1, n+1)]
    # 電車の番号と電車の前後を格納するリスト
    # 例：[1, 2, 3, 4, 5, 6, 7]
    #     [0, 1, 2, 3, 4, 5, 6]
    #     [1, 2, 3, 4, 5, 6, 0]
    #     [1, 2, 3, 4, 5, 0, 6]
    #     [1, 2, 3, 4, 0, 5, 6]
    #     [1, 2, 3, 0, 4, 5, 6]
    #     [1, 2, 0, 3, 4, 5, 6]
    #     [1, 0, 2, 3, 4, 5, 6]
    #     [0, 1, 2, 3, 4, 5, 6]
    #     [1, 2, 3, 4, 5, 6, 0]
    #     [1, 5, 2, 3, 4, 0, 6]
    #     [1, 5, 2, 3, 4, 6, 0]
    #     [1, 5, 2, 3, 0, 4, 6]
    #     [1, 5, 2, 0, 3, 4, 6]
    #     [1, 5, 0, 2, 3, 4, 6]
    #     [1, 0, 5, 2, 3, 4, 6]
    #     [0, 1, 5, 2, 3, 4, 6]
    #     [1, 5, 2,

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    #入力
    N,Q = map(int,input().split())
    train = [0]*N
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            train[query[2]-1] = query[1]
        elif query[0] == 2:
            train[query[2]-1] = 0
        else:
            ans = []
            ans.append(query[1])
            while train[ans[-1]-1] != 0:
                ans.append(train[ans[-1]-1])
            print(len(ans),*ans)

=======
Suggestion 9

def main():
    #入力
    N, Q = map(int, input().split())
    #電車の番号を格納するリスト
    train = [i for i in range(N)]
    #電車の後部と前部を格納するリスト
    train_next = [i+1 for i in range(N)]
    train_next[-1] = -1
    train_prev = [i-1 for i in range(N)]
    train_prev[0] = -1
    #電車の連結成分の先頭を格納するリスト
    train_head = [i for i in range(N)]
    #電車の連結成分の末尾を格納するリスト
    train_tail = [i for i in range(N)]
    #クエリ処理
    for i in range(Q):
        #クエリの種類を取得
        query = input().split()
        #クエリの種類を取得
        c = int(query[0])
        #クエリの種類が1の場合
        if c == 1:
            #x,yを取得
            x, y = map(int, query[1:])
            x -= 1
            y -= 1
            #xの連結成分の末尾の後ろにyの連結成分をつなげる
            train_next[train_tail[x]] = train_head[y]
            train_prev[train_head[y]] = train_tail[x]
            #yの連結成分の末尾をxの連結成分の末尾にする
            train_tail[x] = train_tail[y]
        #クエリの種類が2の場合
        elif c == 2:
            #x,yを取得
            x, y = map(int, query[1:])
            x -= 1
            y -= 1
            #xの連結成分の末尾の後ろをyの連結成分の先頭にする
            train_next[train_tail[x]] = train_head[y

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    # 連結成分のリスト
    # 連結成分は、その連結成分に含まれる電車の番号のリスト
    # 連結成分のリストは、連結成分のリストのインデックスをその連結成分の番号とする
    CC = []
    # 電車のリスト
    # 電車は、その電車の連結成分の番号と、その電車の直前に連結している電車の番号を持つ
    # 電車のリストは、電車のリストのインデックスをその電車の番号とする
    T = []
    for i in range(N):
        # 電車の初期化
        # 連結成分のリストに、その電車の番号のみのリストを追加する
        CC.append([i])
        # 電車のリストに、その電車の連結成分の番号と、その電車の直前に連結している電車の番号を持つリストを追加する
        T.append([i, -1])
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            # 電車 x の後部と、電車 y の前部を連結させる
            # 連結成分のリストのインデックスを、その電車の連結成分の番号とする
            # 電車 x の連結成分の番号を取得する
            x = T[query[1] - 1][0]
            # 電車 y の連結成分の番号を取得する
