def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0]*N
    X[0] = A[0]
    for i in range(1,N):
        if (A[i] - X[i-1]) <= K:
            X[i] = A[i]
        elif (B[i] - X[i-1]) <= K:
            X[i] = B[i]
        else:
            print("No")
            exit()
    print("Yes")
