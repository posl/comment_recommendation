def main():
    #输入
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        #print(a,b)
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #计算
    #定义一个列表用来存储是否是好的观测站
    good = [True]*N
    #print(good)
    #遍历所有的道路
    for i in range(M):
        #print(i)
        #print(H[A[i]-1],H[B[i]-1])
        #print(A[i],B[i])
        #print(good[A[i]-1],good[B[i]-1])
        #print(good[A[i]-1] and good[B[i]-1])
        #print(H[A[i]-1] <= H[B[i]-1])
        #print(H[A[i]-1] >= H[B[i]-1])
        #print(H[A[i]-1] <= H[B[i]-1] and H[A[i]-1] >= H[B[i]-1])
        #print(good[A[i]-1] and good[B[i]-1] and H[A[i]-1] <= H[B[i]-1] and H[A[i]-1] >= H[B[i]-1])
        if good[A[i]-1] and good[B[i]-1] and H[A[i]-1] <= H[B[i]-1] and H[A[i]-1] >= H[B[i]-1]:
            good[A[i]-1] = False
            good[B[i]-1] = False
            #print(good)
        elif good[A[i]-1] and H[A[i]-1] >= H[B[i]-1]:
            good[A[i]-1] = False
            #print(good)
        elif good[B[i]-1] and H[A[i]-1] <= H[B[i]-1]:
            good[B[i]-1] = False
            #print(good)
    #print(good)
    #输出
    print(good.count(True))
