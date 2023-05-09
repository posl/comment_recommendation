def main():
    N = int(input())
    W = list(map(int, input().split()))
    S1 = 0
    S2 = sum(W)
    min_diff = S2 - S1
    for i in range(N-1):
        S1 += W[i]
        S2 -= W[i]
        diff = abs(S1 - S2)
        min_diff = min(min_diff, diff)
    print(min_diff)

if __name__ == '__main__':
    main()