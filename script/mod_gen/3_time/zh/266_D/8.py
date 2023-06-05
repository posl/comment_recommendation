def main():
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    #print(N)
    #print(T)
    #print(X)
    #print(A)
    #最大值
    #max = 0
    #for i in range(1, N):
    #    if T[i] > T[max]:
    #        max = i
    #print(max)
    #print(T[max])
    #最大值
    max = 0
    for i in range(1, N):
        if T[i] > T[max]:
            max = i
        elif T[i] == T[max]:
            if A[i] > A[max]:
                max = i
    #print(max)
    #print(T[max])
    #print(A[max])
    #最大值
    max = 0
    for i in range(1, N):
        if T[i] > T[max]:
            max = i
        elif T[i] == T[max]:
            if A[i] > A[max]:
                max = i
            elif A[i] == A[max]:
                if X[i] < X[max]:
                    max = i
    #print(max)
    #print(T[max])
    #print(A[max])
    #print(X[max])
    #最大值
    max = 0
    for i in range(1, N):
        if T[i] > T[max]:
            max = i
        elif T[i] == T[max]:
            if A[i] > A[max]:
                max = i
            elif A[i] == A[max]:
                if X[i] < X[max]:
                    max = i
                elif X[i] == X[max]:
                    if A[i] < A[max]:
                        max = i
    #print(max)
    #print(T[max])
    #print(A[max])
    #print(X[max])
    #最大值
    max = 0
    for i in range(1, N):
        if T[i] > T[max]:
            max = i
        elif T[i] == T[max]:
            if A[i] > A[max]:
                max = i
            elif A

if __name__ == '__main__':
    main()