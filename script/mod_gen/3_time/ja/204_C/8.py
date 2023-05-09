def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    #print(N,M)
    #print(AB)
    # 都市の組み合わせはN*(N-1)/2
    # それぞれの組み合わせに対して、スタート地点とゴール地点を決める
    # スタート地点とゴール地点の組み合わせが何通りあるかを計算する
    # 都市の組み合わせの数
    city_combination = int(N*(N-1)/2)
    # スタート地点とゴール地点の組み合わせの数
    start_goal_combination = 0
    for i in range(city_combination):
        for j in range(M):
            if i+1 == AB[j][0] or i+1 == AB[j][1]:
                #print(i+1,AB[j][0],AB[j][1])
                start_goal_combination += 1
                break
    #print(city_combination,start_goal_combination)
    print(city_combination - start_goal_combination)

if __name__ == '__main__':
    main()