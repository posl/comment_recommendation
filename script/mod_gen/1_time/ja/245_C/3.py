def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0]*N
    for i in range(N):
        if i == 0:
            X[i] = A[i]
        else:
            if abs(A[i]-X[i-1]) > K and abs(B[i]-X[i-1]) > K:
                print("No")
                return
            elif abs(A[i]-X[i-1]) > K:
                X[i] = B[i]
            elif abs(B[i]-X[i-1]) > K:
                X[i] = A[i]
            else:
                if A[i] < B[i]:
                    X[i] = A[i]
                else:
                    X[i] = B[i]
    print("Yes")

if __name__ == '__main__':
    main()