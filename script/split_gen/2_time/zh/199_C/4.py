def main():
    N = int(input())
    S = input()
    Q = int(input())
    #print(N)
    #print(S)
    #print(Q)
    #print("S[:N] = ", S[:N])
    #print("S[N:] = ", S[N:])
    for i in range(Q):
        T, A, B = map(int, input().split())
        #print("T = ", T, "A = ", A, "B = ", B)
        if T == 1:
            S = S[:A-1] + S[B-1] + S[A:B-1] + S[A-1] + S[B:]
        else:
            S = S[N:] + S[:N]
        #print("S = ", S)
    print(S)
