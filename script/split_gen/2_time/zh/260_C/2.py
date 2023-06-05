def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = []
    for i in range(N):
        C.append([A[i]+B[i],A[i],B[i],i+1])
    C.sort(reverse=True)
    #print(C)
    ans = []
    for i in range(X):
        ans.append(C[i][3])
    #print(ans)
    C = C[X:]
    C.sort(key=lambda x:(x[1],x[3]),reverse=True)
    #print(C)
    for i in range(Y):
        ans.append(C[i][3])
    #print(ans)
    C = C[Y:]
    C.sort(key=lambda x:(x[0],x[3]),reverse=True)
    #print(C)
    for i in range(Z):
        ans.append(C[i][3])
    #print(ans)
    ans.sort()
    #print(ans)
    for i in range(len(ans)):
        print(ans[i])
main()
