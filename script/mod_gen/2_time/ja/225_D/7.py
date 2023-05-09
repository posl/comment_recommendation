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

if __name__ == '__main__':
    main()