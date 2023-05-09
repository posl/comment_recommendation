def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    X = [0] * N
    #Xの初期値を決める
    for i in range(N):
        if A[i] <= B[i]:
            X[i] = A[i]
        else:
            X[i] = B[i]
    #Xを決める
    for i in range(N-1):
        if X[i] == A[i] and X[i+1] == A[i+1]:
            if abs(A[i]-B[i]) <= K:
                X[i+1] = B[i+1]
            else:
                X[i+1] = A[i+1]
        elif X[i] == B[i] and X[i+1] == B[i+1]:
            if abs(A[i]-B[i]) <= K:
                X[i+1] = A[i+1]
            else:
                X[i+1] = B[i+1]
        else:
            continue
    #Xを出力する
    for i in range(N):
        print(X[i],end=" ")
    print()
