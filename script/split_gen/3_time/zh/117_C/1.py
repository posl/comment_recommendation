def solution(N,M,X):
    X.sort()
    if N==1:
        return 0
    else:
        if X[M-1]>0:
            return X[M-1]-X[1]
        else:
            return abs(X[M-2]-X[0])
N,M=map(int,input().split())
X=list(map(int,input().split()))
print(solution(N,M,X))
