def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0] * N
    for i in range(N):
        if i == 0:
            X[i] = A[i]
            continue
        if A[i] <= K + X[i - 1]:
            X[i] = A[i]
        elif B[i] <= K + X[i - 1]:
            X[i] = B[i]
        else:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()