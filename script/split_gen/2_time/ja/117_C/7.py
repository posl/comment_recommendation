def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    #print(X[M-1]-X[0])
    diff = [0]*(M-1)
    for i in range(M-1):
        diff[i] = X[i+1]-X[i]
    diff.sort()
    #print(diff)
    if N >= M:
        print(0)
    else:
        for i in range(M-N):
            #print(diff[i])
            X[M-1] -= diff[i]
        print(X[M-1]-X[0])
