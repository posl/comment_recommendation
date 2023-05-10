def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    #print(n, k, q)
    #print(a)
    #print(l)
    #aのリストに対応するコマを追加
    ka = []
    for i in range(n):
        ka.append(0)
    for i in range(k):
        ka[a[i]-1] = 1
    #print(ka)
    #lのリストを逆順にして、操作を行う
    for i in range(q-1, -1, -1):
        #print(l[i])
        #print(ka)
        #print(ka[l[i]-1])
        #print(ka[l[i]])
        if ka[l[i]-1] == 1 and ka[l[i]] == 0:
            ka[l[i]] = 1
            ka[l[i]-1] = 0
        #print(ka)
        #print("")
    #kaのリストからコマのあるマスを出力
    for i in range(n):
        if ka[i] == 1:
            print(i+1, end=" ")
    print("")

if __name__ == '__main__':
    main()