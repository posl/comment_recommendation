def main():
    #输入
    N = int(input())
    A = list(map(int,input().split()))
    #初始化
    P = 0
    #遍历
    for i in range(N):
        #将方格上的每个棋子向前推进A[i]个方格
        for j in range(i+1):
            #如果目标方格不存在（即x+A_i大于或等于4）的棋子，则将其移除
            if A[j] + j >= 4:
                P += 1
                A[j] = 0
            else:
                A[j] += A[i]
        #在0号方格放一个棋子，现在0号方格有一个棋子。
        A[0] += 1
    print(P)
