def main():
    N, Q = map(int, input().split())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    #print(N, Q)
    #print(T)
    #print(A)
    #print(B)
    follow = [[0 for i in range(N)] for j in range(N)]
    for i in range(Q):
        if T[i] == 1:
            follow[A[i] - 1][B[i] - 1] = 1
        elif T[i] == 2:
            follow[A[i] - 1][B[i] - 1] = 0
        elif T[i] == 3:
            if follow[A[i] - 1][B[i] - 1] == 1:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()