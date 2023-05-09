def main():
    N = int(input())
    W = list(map(int, input().split()))
    #print(N)
    #print(W)
    S = sum(W)
    #print(S)
    S1 = 0
    S2 = S
    min = S
    for T in range(1, N):
        S1 += W[T-1]
        S2 -= W[T-1]
        #print(T, S1, S2)
        if abs(S1 - S2) < min:
            min = abs(S1 - S2)
    print(min)
main()
