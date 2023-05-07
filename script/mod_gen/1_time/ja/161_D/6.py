def main():
    K = int(input())
    #print(K)
    #ルンルン数を格納するリスト
    runrun = []
    #ルンルン数の探索
    #1桁目は1～9
    for i in range(1, 10):
        #print(i)
        runrun.append(i)
        #print(runrun)
        #2桁目は1～9
        for j in range(1, 10):
            #print(j)
            #print(i, j)
            #print(abs(i - j))
            #差の絶対値が1以下の場合のみルンルン数に追加
            if abs(i - j) <= 1:
                runrun.append(int(str(i) + str(j)))
                #print(runrun)
                #3桁目は1～9
                for k in range(1, 10):
                    #print(k)
                    #print(i, j, k)
                    #print(abs(j - k))
                    #差の絶対値が1以下の場合のみルンルン数に追加
                    if abs(j - k) <= 1:
                        runrun.append(int(str(i) + str(j) + str(k)))
                        #print(runrun)
                        #4桁目は1～9
                        for l in range(1, 10):
                            #print(l)
                            #print(i, j, k, l)
                            #print(abs(k - l))
                            #差の絶対値が1以下の場合のみルンルン数に追加
                            if abs(k - l) <= 1:
                                runrun.append(int(str(i) + str(j) + str(k) + str(l)))
                                #print(runrun)
                                #5桁目は1～9
                                for m in range(1, 10):
                                    #print(m)
                                    #print(i, j, k, l, m)
                                    #print(abs(l - m))
                                    #差の絶対値が1以下の場合のみルンルン数に追加
                                    if abs(l - m) <= 1:
                                        runrun.append(int(str(i) + str

if __name__ == '__main__':
    main()