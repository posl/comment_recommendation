def main():
    N, M, Q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(Q)]
    
    for L, R in query:
        #箱の大きさのリストを作成
        x = X[:L-1] + X[R:]
        #荷物の価値のリストを作成
        v = [i[1] for i in wv]
        #荷物の大きさのリストを作成
        w = [i[0] for i in wv]
        #箱の大きさのリストを小さい順に並べ替える
        x.sort()
        #荷物の大きさのリストを小さい順に並べ替える
        w.sort()
        #荷物の価値のリストを大きい順に並べ替える
        v.sort(reverse=True)
        
        #荷物の価値のリストの大きさを取得
        v_len = len(v)
        #箱の大きさのリストの大きさを取得
        x_len = len(x)
        
        #荷物の価値のリストの大きさが箱の大きさのリストの大きさより大きい場合、
        #箱の大きさのリストの大きさを荷物の価値のリストの大きさにする
        if v_len > x_len:
            v_len = x_len
        
        #荷物の価値のリストの大きさが0より大きい場合、
        if v_len > 0:
            #荷物の価値のリストの大きさ分繰り返す
            for i in range(v_len):
                #箱の大きさのリストの要素が荷物の大きさのリストの要素より小さい場合、
                if x[i

if __name__ == '__main__':
    main()