def main():
    n,k,q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    #print(n,k,q)
    #print(a)
    #print(l)
    #初始化
    #棋子位置
    chess = [0] * n
    for i in a:
        chess[i-1] = 1
    #print(chess)
    #操作
    for i in l:
        #print(i)
        #print(chess)
        if chess[i-1] == 1:
            #print("ok")
            continue
        else:
            #print("no")
            for j in range(i,n):
                #print(j)
                if chess[j] == 0:
                    chess[j] = 1
                    break
            #print(chess)
    #print(chess)
    #打印结果
    for i in range(n):
        if chess[i] == 1:
            print(i+1, end=" ")

if __name__ == '__main__':
    main()