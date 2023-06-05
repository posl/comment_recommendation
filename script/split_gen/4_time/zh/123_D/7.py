def main():
    X,Y,Z,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    #print(X,Y,Z,K)
    #print(A)
    #print(B)
    #print(C)
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    #print(A)
    #print(B)
    #print(C)
    ans = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                if (i+1)*(j+1)*(k+1) > K:
                    break
                ans.append(A[i]+B[j]+C[k])
    ans.sort(reverse=True)
    #print(ans)
    for i in range(K):
        print(ans[i])
    return
