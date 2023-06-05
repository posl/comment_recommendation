def main():
    N, Q = map(int, input().split())
    S = input()
    #print(N, Q, S)
    A = [0] * (N+1)
    C = [0] * (N+1)
    G = [0] * (N+1)
    T = [0] * (N+1)
    for i in range(N):
        A[i+1] = A[i]
        C[i+1] = C[i]
        G[i+1] = G[i]
        T[i+1] = T[i]
        if S[i] == 'A':
            A[i+1] += 1
        elif S[i] == 'C':
            C[i+1] += 1
        elif S[i] == 'G':
            G[i+1] += 1
        else:
            T[i+1] += 1
    #print(A)
    #print(C)
    #print(G)
    #print(T)
    for i in range(Q):
        l, r = map(int, input().split())
        #print(l, r)
        print(A[r] - A[l-1], C[r] - C[l-1], G[r] - G[l-1], T[r] - T[l-1])

if __name__ == '__main__':
    main()