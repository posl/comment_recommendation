def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = []
    for i in range(N):
        if A[i] <= B[i]:
            X.append(A[i])
        else:
            if B[i] + K >= A[i]:
                X.append(B[i])
            else:
                print("No")
                return
    print("Yes")
