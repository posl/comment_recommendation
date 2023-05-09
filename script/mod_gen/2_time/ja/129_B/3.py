def main():
    N = int(input())
    W = list(map(int, input().split()))
    S1 = 0
    S2 = sum(W)
    diff = S2 - S1
    for i in range(N-1):
        S1 += W[i]
        S2 -= W[i]
        diff = min(diff, abs(S2-S1))
    print(diff)

if __name__ == '__main__':
    main()