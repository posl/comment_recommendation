def main():
    L, Q = map(int, input().split())
    q_list = []
    for i in range(Q):
        c, x = map(int, input().split())
        q_list.append((c, x))
    #print(q_list)
    #print(L, Q)
    #print(q_list[0][0])
    #木材の長さを管理する配列
    woods = [L]
    #print(woods)
    #クエリの回数分繰り返す
    for i in range(Q):
        #print("i:", i)
        #print("woods:", woods)
        #print("q_list:", q_list[i])
        #クエリが1の場合
        if q_list[i][0] == 1:
            #print("q_list[i][1]:", q_list[i][1])
            #print("woods.index(q_list[i][1]):", woods.index(q_list[i][1]))
            #print("woods[woods.index(q_list[i][1])]:", woods[woods.index(q_list[i][1])])
            #print("woods[woods.index(q_list[i][1])] - q_list[i][1]:", woods[woods.index(q_list[i][1])] - q_list[i][1])
            #print("q_list[i][1] - woods[woods.index(q_list[i][1]) - 1]:", q_list[i][1] - woods[woods.index(q_list[i][1]) - 1])
            #print("woods[woods.index(q_list[i][1])] - q_list[i][1] + q_list[i][1] - woods[woods.index(q_list[i][1]) - 1]:", woods[woods.index(q_list[i][1])] - q_list[i][1] + q_list[i][1] - woods[woods.index(q_list[i][1]) - 1])
            #print("woods[woods.index(q_list[i][1])] - q_list[i][1] + q_list[i][1] - woods[woods.index(q_list[i][1]) - 1] - 1:", woods[woods.index(q_list[i][1])] - q_list[i][1] + q_list[i][1] - woods[woods.index(q_list[i][1]) - 1] - 1)
            #print("woods

if __name__ == '__main__':
    main()