def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    X = [0]*N
    for i in range(N):
        if i==0:
            if A[i] > B[i]:
                X[i] = B[i]
            else:
                X[i] = A[i]
        else:
            if A[i] > B[i]:
                if B[i] <= X[i-1]+K:
                    X[i] = B[i]
                else:
                    X[i] = A[i]
            else:
                if A[i] <= X[i-1]+K:
                    X[i] = A[i]
                else:
                    X[i] = B[i]
    if X[N-1] - X[0] <= K:
        print("Yes")
    else:
        print("No")
