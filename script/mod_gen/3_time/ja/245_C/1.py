def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0] * N
    for i in range(N):
        if i == 0:
            if A[i] <= B[i]:
                X[i] = A[i]
            else:
                X[i] = B[i]
        else:
            if X[i - 1] + K >= A[i]:
                X[i] = A[i]
            elif X[i - 1] + K >= B[i]:
                X[i] = B[i]
            else:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()