Synthesizing 10/10 solutions

=======
Suggestion 1

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    train = [i for i in range(N+1)]
    for i in range(Q):
        c, x, y = map(int, input().split())
        if c == 1:
            train[y] = x
        elif c == 2:
            train[x] = y
        else:
            ans = []
            while x != 0:
                ans.append(x)
                x = train[x]
            print(len(ans), *ans)

main()

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    train = [[i, i, i] for i in range(N + 1)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if len(query) == 3:
            if query[0] == 1:
                # query[1]の後ろにquery[2]をつなげる
                train[query[1]][2] = query[2]
                train[query[2]][0] = query[1]
            else:
                # query[1]の後ろを切り離す
                train[train[query[1]][2]][0] = query[1]
                train[query[1]][2] = query[1]
        else:
            # query[1]が含まれる連結成分に属する電車の番号を出力
            ans = []
            i = query[1]
            while train[i][0] != i:
                ans.append(i)
                i = train[i][0]
            ans.append(i)
            print(len(ans), *ans)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    train = [0] * (N + 1)
    for i in range(1, N+1):
        train[i] = i

    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[query[2]] = train[query[1]]
        if query[0] == 2:
            train[query[2]] = query[2]
        if query[0] == 3:
            ans = []
            for j in range(1, N+1):
                if train[j] == train[query[1]]:
                    ans.append(j)
            print(len(ans), *ans)

=======
Suggestion 5

def main():
    N,Q = list(map(int,input().split()))
    train = [i for i in range(N+1)]
    #print(train)
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            #print("query[0] == 1")
            x = train[query[1]]
            y = train[query[2]]
            #print("x = train[query[1]]",x)
            #print("y = train[query[2]]",y)
            train[x] = y
            #print("train[x] = y",train[x])
        elif query[0] == 2:
            #print("query[0] == 2")
            x = train[query[1]]
            y = train[query[2]]
            #print("x = train[query[1]]",x)
            #print("y = train[query[2]]",y)
            train[x] = x
            #print("train[x] = x",train[x])
        else:
            #print("query[0] == 3")
            x = train[query[1]]
            #print("x = train[query[1]]",x)
            ans = [query[1]]
            while x != train[x]:
                ans.append(train[x])
                x = train[x]
            print(len(ans),*ans)
            #print("len(ans),*ans",len(ans),*ans)
    return

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    N,Q = map(int,input().split())
    A = [0]*N
    for i in range(N):
        A[i] = i
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            x,y = query[1],query[2]
            A[x-1] = y-1
        elif query[0] == 2:
            x,y = query[1],query[2]
            A[x-1] = x-1
        else:
            x = query[1]
            ans = []
            while True:
                ans.append(x)
                x = A[x-1]+1
                if x == 0:
                    break
            print(len(ans),*ans)
    return

=======
Suggestion 7

def main():
    N,Q = map(int,input().split())
    train = [i+1 for i in range(N)]
    train.insert(0,0)
    train.append(0)
    #print(train)
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            train[query[2]] = train[query[1]]
        elif query[0] == 2:
            train[query[1]] = query[2]
        elif query[0] == 3:
            ans = []
            ans.append(query[1])
            while train[query[1]] != 0:
                ans.append(train[query[1]])
                query[1] = train[query[1]]
            print(len(ans),*ans)

=======
Suggestion 8

def main():
    #入力
    N,Q = map(int,input().split())
    #電車の番号を格納するリスト
    train = [i for i in range(N+1)]
    #電車の前後を格納するリスト
    prev = [i for i in range(N+1)]
    next = [i for i in range(N+1)]
    #クエリを処理する
    for i in range(Q):
        query = list(map(int,input().split()))
        if(query[0] == 1):
            #xの後ろにyをつなぐ
            x = query[1]
            y = query[2]
            #xの後ろにyをつなぐ
            next[x] = y
            #yの前にxをつなぐ
            prev[y] = x
        elif(query[0] == 2):
            #xの後ろのyを切り離す
            x = query[1]
            y = query[2]
            #xの後ろのyを切り離す
            next[x] = y
            #yの前のxを切り離す
            prev[y] = x
        elif(query[0] == 3):
            #xを含む連結成分の番号を先頭から順に出力
            x = query[1]
            #出力するリスト
            output = []
            #xの前の電車を探す
            while(prev[x] != x):
                x = prev[x]
            #xの後ろの電車を探す
            while(next[x] != x):
                output.append(x)
                x = next[x]
            output.append(x)
            print(len(output),*output)

=======
Suggestion 9

def main():
    #入力
    N, Q = map(int, input().split())
    #電車の連結情報を格納するリスト
    #連結情報を格納するリストの要素は、次の3つの要素のタプルで表現する。
    #リストの要素は、(前の電車の番号, 後の電車の番号, 連結成分の番号)となっている。
    #前の電車の番号と後の電車の番号は、連結している電車の番号を格納している。
    #連結成分の番号は、連結成分の番号を格納している。
    #電車の番号は、1からNまでの番号が振られている。
    #連結成分の番号は、1からNまでの番号が振られている。
    #電車の前後に連結している電車が存在しない場合は、-1が格納されている。
    #連結成分の番号は、連結成分の先頭の電車の番号と同じとする。
    #例えば、(1, 2, 1)は、電車1の後ろに電車2が連結していることを表す。
    #電車1の前に連結している電車は存在しないため、1の前の電車の番号は-1となっている。
    #連結成分の番号は、連結成分の先頭の電車の番号と同じとする。
    #例えば、(1, 2, 1)は、電車1の後ろに電

=======
Suggestion 10

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
