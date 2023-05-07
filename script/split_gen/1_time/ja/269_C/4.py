def main():
    N = int(input())
    #Nを2進数に変換
    N_2 = bin(N)
    N_2 = N_2[2:]
    #print(N_2)
    #Nの1の位置を取得
    N_1 = []
    for i in range(len(N_2)):
        if N_2[i] == "1":
            N_1.append(i)
    #print(N_1)
    #Nの1の位置の数だけforループ
    for i in range(2**len(N_1)):
        #print(i)
        #iを2進数に変換
        i_2 = bin(i)
        i_2 = i_2[2:]
        #print(i_2)
        #iの1の位置を取得
        i_1 = []
        for j in range(len(i_2)):
            if i_2[j] == "1":
                i_1.append(j)
        #print(i_1)
        #iの1の位置がNの1の位置の部分集合になっているか確認
        if set(i_1) <= set(N_1):
            print(i)
