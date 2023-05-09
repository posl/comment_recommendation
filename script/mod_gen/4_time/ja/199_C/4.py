def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t,a,b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    
    #print(T)
    #print(A)
    #print(B)
    #print(S[:N])
    #print(S[N:])
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                a = A[i] - 1
            else:
                a = A[i] - N - 1
            if B[i] <= N:
                b = B[i] - 1
            else:
                b = B[i] - N - 1
            #print(a,b)
            S = S[:a] + S[b] + S[a+1:b] + S[a] + S[b+1:]
        else:
            S = S[N:] + S[:N]
        #print(S[:N])
        #print(S[N:])
    print(S)

if __name__ == '__main__':
    main()