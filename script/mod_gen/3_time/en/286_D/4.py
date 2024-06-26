def main():
    N, X = map(int, input().split())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        if A[i]*B[i] >= X:
            B[i] = X//A[i]
            X -= A[i]*B[i]
        else:
            X -= A[i]*B[i]
    if X == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()