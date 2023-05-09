def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    #print(N)
    #print(S)
    #print(Q)
    #print(T)
    #print(A)
    #print(B)
    for i in range(Q):
        if T[i] == 1:
            a = S[A[i]-1]
            b = S[B[i]-1]
            S = S[:A[i]-1] + b + S[A[i]:B[i]-1] + a + S[B[i]:]
        else:
            S = S[N:] + S[:N]
    print(S)

if __name__ == '__main__':
    main()