def main():
    N,M = map(int,input().split())
    l = []
    for i in range(M):
        l.append(list(map(int,input().split())))
    p = list(map(int,input().split()))
    #print(l)
    #print(p)
    #電球の個数
    light = 0
    #スイッチのon/offの組み合わせ
    count = 0
    #電球の個数を数える
    for i in range(M):
        light += l[i][0]
    #スイッチのon/offの組み合わせを数える
    for i in range(2**N):
        #on/offの組み合わせをlistにする
        on_off = list(format(i,'0{}b'.format(N)))
        #print(on_off)
        #電球の個数分だけループ
        for j in range(M):
            #電球の個数分のスイッチをループ
            for k in range(1,l[j][0]+1):
                #print(on_off[l[j][k]-1])
                #スイッチがonの時
                if on_off[l[j][k]-1] == '1':
                    count += 1
            #print(count)
            #print(p[j])
            #スイッチのonの個数が奇数個の時
            if count % 2 == 1:
                #print('奇数')
                #電球が点灯している時
                if p[j] == 1:
                    count = 0
                #電球が点灯していない時
                else:
                    count = 0
                    break
            #スイッチのonの個数が偶数個の時
            else:
                #print('偶数')
                #電球が点灯している時
                if p[j] == 0:
                    count = 0
                #電球が点灯していない時
                else:
                    count = 0
                    break
        #print(count)
        #print(light)
        #電球の

if __name__ == '__main__':
    main()