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
