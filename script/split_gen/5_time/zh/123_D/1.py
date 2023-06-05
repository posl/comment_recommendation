def solve():
    #读取输入
    X,Y,Z,K=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    C=list(map(int,input().split()))
    #将A,B,C分别按照降序排列
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    #A,B,C的前K个元素的组合
    ans=[]
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                if (i+1)*(j+1)*(k+1)<=K:
                    ans.append(A[i]+B[j]+C[k])
                else:
                    break
    #将ans降序排列
    ans.sort(reverse=True)
    #输出
    for i in range(K):
        print(ans[i])
