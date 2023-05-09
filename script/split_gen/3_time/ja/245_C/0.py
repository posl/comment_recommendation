def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0] * N
    for i in range(N):
        if i == 0:
            X[i] = min(A[i], B[i])
        else:
            if abs(A[i] - X[i-1]) <= K and abs(B[i] - X[i-1]) <= K:
                X[i] = min(A[i], B[i])
            elif abs(A[i] - X[i-1]) <= K:
                X[i] = A[i]
            elif abs(B[i] - X[i-1]) <= K:
                X[i] = B[i]
            else:
                print("No")
                return
    print("Yes")
    return
