def main():
    K = int(input())
    S = input()
    T = input()
    S = S[0:4]
    T = T[0:4]
    S = S + '#'
    T = T + '#'
    S = list(S)
    T = list(T)
    S = [int(i) for i in S]
    T = [int(i) for i in T]
    S = sorted(S)
    T = sorted(T)
    A = [0,0,0,0,0,0,0,0,0,0]
    B = [0,0,0,0,0,0,0,0,0,0]
    for i in range(1,10):
        A[i] = S.count(i)
        B[i] = T.count(i)
    C = [0,0,0,0,0,0,0,0,0,0]
    D = [0,0,0,0,0,0,0,0,0,0]
    for i in range(1,10):
        C[i] = K - A[i] - B[i]
        D[i] = K - A[i] - B[i]
    A[0] = 9*K - 8
    B[0] = 9*K - 8
    C[0] = 9*K - 9
    D[0] = 9*K - 9
    E = [0,0,0,0,0,0,0,0,0,0]
    F = [0,0,0,0,0,0,0,0,0,0]
    for i in range(1,10):
        E[i] = A[i]*C[i]
        F[i] = B[i]*D[i]
    G = 0
    H = 0
    for i in range(1,10):
        G += i*10**E[i]
        H += i*10**F[i]
    I = 0
    J = 0
    for i in range(1,10):
        for j in range(1,10):
            if i == j:
                I += i*10**(E[i]+E[j]-1)*C[i]*D[j]
                J += i*10**(
