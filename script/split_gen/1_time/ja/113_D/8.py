def func():
    #横線を引くところのリスト
    #yoko = [[0,0],[0,1],[1,1],[1,2],[2,2],[2,3],[3,3]]
    yoko = []
    for i in range(1,W):
        yoko.append([i,i])
        yoko.append([i,i+1])
    yoko.append([W,W])
    #print(yoko)
    #横線を引かないところのリスト
    yoko_not = []
    for i in range(1,W+1):
        yoko_not.append([i,i])
    #print(yoko_not)
    #横線を引くところのリストの中からK個選ぶ場合の数
    #yoko_comb = list(itertools.combinations(yoko,K))
    yoko_comb = []
    for i in itertools.combinations(yoko,K):
        yoko_comb.append(i)
    #print(yoko_comb)
    #横線を引かないところのリストの中からW-K個選ぶ場合の数
    #yoko_not_comb = list(itertools.combinations(yoko_not,W-K))
    yoko_not_comb = []
    for i in itertools.combinations(yoko_not,W-K):
        yoko_not_comb.append(i)
    #print(yoko_not_comb)
    #横線を引くところのリストの中からK個選ぶ場合の数の中から
    #横線を引かないところのリストの中からW-K個選ぶ場合の数を引いた数
    #print(len(yoko_comb))
    #print(len(yoko_not_comb))
    #print(len(yoko_comb)-len(yoko_not_comb))
    #答え
    ans = len(yoko_comb)-len(yoko_not_comb)
    print(ans%1000000007)
