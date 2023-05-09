def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print("N, X", N, X)
    #print("A", A)
    #print("B", B)
    for i in range(N):
        if X >= A[i] * B[i]:
            X -= A[i] * B[i]
        else:
            X -= X // A[i] * A[i]
    if X == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()