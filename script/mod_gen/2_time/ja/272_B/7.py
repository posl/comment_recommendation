def main():
    N,M = map(int,input().split())
    #print(N,M)
    #print("")
    #舞踏会の参加者をリストに格納
    list = []
    for i in range(M):
        l = list(map(int,input().split()))
        list.append(l)
    #print(list)
    #print("")
    #参加者のリストを集合に変換
    set_list = []
    for i in range(M):
        s = set(list[i])
        set_list.append(s)
    #print(set_list)
    #print("")
    #集合の積を求める
    s = set_list[0]
    for i in range(1,M):
        s = s & set_list[i]
    #print(s)
    if len(s) == 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()