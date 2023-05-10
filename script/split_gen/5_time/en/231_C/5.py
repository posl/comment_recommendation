def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    X = []
    for i in range(Q):
        X.append(int(input()))
    #print(N,Q,A,X)
    for i in range(Q):
        for j in range(N):
            if X[i] <= A[j]:
                print(N-j)
                break
