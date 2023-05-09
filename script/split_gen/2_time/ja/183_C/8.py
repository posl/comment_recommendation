def solve( N, K, T):
    # write code here
    #print( N, K, T)
    #print( T)
    #print( type(T))
    #print( len(T))
    #print( len(T[0]))
    #print( T[0][0])
    #print( T[0][1])
    #print( T[0][2])
    #print( T[0][3])
    #print( T[1][0])
    #print( T[1][1])
    #print( T[1][2])
    #print( T[1][3])
    #print( T[2][0])
    #print( T[2][1])
    #print( T[2][2])
    #print( T[2][3])
    #print( T[3][0])
    #print( T[3][1])
    #print( T[3][2])
    #print( T[3][3])
    # 順列を生成するライブラリ
    import itertools
    # 都市のリストを作成
    city_list = [i+1 for i in range(N)]
    # 順列を作成
    perm_list = list(itertools.permutations(city_list))
    #print( perm_list)
    # 経路の数をカウントする変数
    count = 0
    # 都市の順列を1つずつ取り出す
    for perm in perm_list:
        #print( perm)
        #print( type(perm))
        # 移動時間の合計をカウントする変数
        sum_time = 0
        # 都市の順列から1つずつ都市を取り出す
        for i in range(N):
            #print( i)
            #print( type(i))
            # 都市の順列の最初の都市
            if i == 0:
                #print( "都市の順列の最初の都市")
                #print( perm[i])
                #print( type(perm[i]))
                #print( perm[i]-1)
                #print( type(perm[i]-1))
                #print(
