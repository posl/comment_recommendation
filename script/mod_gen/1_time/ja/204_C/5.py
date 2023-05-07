def main():
    N, M = map(int, input().split())
    #print(N, M)
    AB = []
    for _ in range(M):
        A, B = map(int, input().split())
        AB.append([A, B])
    #print(AB)
    #print(len(AB))
    #都市の組み合わせを作成する
    city = []
    for i in range(N):
        for j in range(N):
            if i != j:
                city.append([i+1, j+1])
    #print(city)
    #print(len(city))
    #都市の組み合わせをループして、道路が通っているかどうかを判定する
    count = 0
    for i in range(len(city)):
        #print(city[i])
        for j in range(len(AB)):
            #print(AB[j])
            if city[i][0] == AB[j][0] and city[i][1] == AB[j][1]:
                #print("通っている")
                break
            elif j == len(AB)-1:
                #print("通っていない")
                count += 1
    print(count)

if __name__ == '__main__':
    main()