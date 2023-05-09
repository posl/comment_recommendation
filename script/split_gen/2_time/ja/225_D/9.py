def main():
    N,Q = map(int,input().split())
    #電車の前後の連結関係を表すリスト
    train = [None]*(N+1)
    #電車の前後の連結関係を表すリスト
    train_rev = [None]*(N+1)
    for i in range(N+1):
        train[i] = i
        train_rev[i] = i
    #電車の連結成分を表すリスト
    train_group = [None]*(N+1)
    for i in range(N+1):
        train_group[i] = i
    #電車の連結成分の要素数を表すリスト
    train_group_count = [1]*(N+1)
    #クエリの処理
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            x = query[1]
            y = query[2]
            #xの後ろにyを連結
            train[x] = y
            train_rev[y] = x
            #x,yが連結されている連結成分の要素数を取得
            x_count = train_group_count[train_group[x]]
            y_count = train_group_count[train_group[y]]
            #連結成分の要素数が多い方を残す
            if x_count >= y_count:
                #yの連結成分の要素数をxの連結成分に加算
                train_group_count[train_group[x]] += y_count
                #yの連結成分をxの連結成分に統合
                train_group[train_group[y]] = train_group[x]
            else:
                #xの連結成分の要素数をyの連結成分に加算
                train_group_count[train_group[y]] += x_count
                #xの連結成分をyの連結成分に統合
                train_group[train_group[x]] = train_group[y]
        elif query[0] == 2:
            x = query[1
