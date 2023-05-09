def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    X = []
    for a,b in zip(A,B):
        X.append([a,b])
    for i in range(N-1):
        if abs(X[i][0]-X[i+1][0]) <= K:
            X[i+1][0] = X[i][0]
        if abs(X[i][0]-X[i+1][1]) <= K:
            X[i+1][1] = X[i][0]
        if abs(X[i][1]-X[i+1][0]) <= K:
            X[i+1][0] = X[i][1]
        if abs(X[i][1]-X[i+1][1]) <= K:
            X[i+1][1] = X[i][1]
    if X[-1][0] == X[-1][1]:
        print("Yes")
    else:
        print("No")
