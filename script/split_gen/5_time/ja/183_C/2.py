def solve():
    N, K = map(int, input().split())
    T = []
    for i in range(N):
        T.append(list(map(int, input().split())))
    # 都市1を除く
    cities = list(range(2, N+1))
    # 都市1を除く全ての順列を作成
    from itertools import permutations
    perm_cities = list(permutations(cities))
    # 都市1を除く全ての順列について、都市1から出発し、全ての都市を訪問してから都市1に戻るような経路のうち、移動時間の合計がKになるものの数を求める
    ans = 0
    for perm_city in perm_cities:
        # 都市1から出発
        time = 0
        prev_city = 1
        for city in perm_city:
            time += T[prev_city-1][city-1]
            prev_city = city
        # 都市1に戻る
        time += T[prev_city-1][0]
        if time == K:
            ans += 1
    print(ans)
