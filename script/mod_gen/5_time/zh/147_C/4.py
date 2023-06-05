def main():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        Xi = []
        Yi = []
        for j in range(A[i]):
            x,y = map(int,input().split())
            Xi.append(x)
            Yi.append(y)
        X.append(Xi)
        Y.append(Yi)
    ans = 0
    for i in range(1<<N):
        honest = []
        for j in range(N):
            if i & (1<<j):
                honest.append(j+1)
        flag = True
        for j in range(len(honest)):
            for k in range(A[honest[j]-1]):
                if Y[honest[j]-1][k] == 1 and X[honest[j]-1][k] not in honest:
                    flag = False
                    break
                if Y[honest[j]-1][k] == 0 and X[honest[j]-1][k] in honest:
                    flag = False
                    break
            if flag == False:
                break
        if flag == True:
            ans = max(ans,len(honest))
    print(ans)

if __name__ == '__main__':
    main()