def main():
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    S1 = 0
    S2 = S
    for i in range(N):
        S1 += W[i]
        S2 -= W[i]
        if abs(S1 - S2) > abs(S1 - S//2):
            S1 -= W[i]
            S2 += W[i]
    print(abs(S1 - S2))

if __name__ == '__main__':
    main()