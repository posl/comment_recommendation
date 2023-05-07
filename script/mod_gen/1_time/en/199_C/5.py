def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0 for i in range(Q)]
    A = [0 for i in range(Q)]
    B = [0 for i in range(Q)]
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    S = list(S)
    #print(S)
    #print(T)
    #print(A)
    #print(B)
    #print(N)
    #print(Q)
    flag = 0
    for i in range(Q):
        if T[i] == 1:
            if flag == 0:
                S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
            else:
                if A[i] <= N:
                    A[i] = A[i] + N
                else:
                    A[i] = A[i] - N
                if B[i] <= N:
                    B[i] = B[i] + N
                else:
                    B[i] = B[i] - N
                S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
        else:
            if flag == 0:
                flag = 1
            else:
                flag = 0
    if flag == 1:
        S = S[N:] + S[:N]
    print(''.join(S))

if __name__ == '__main__':
    main()