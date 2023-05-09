def main():
    N = int(input())
    W = list(map(int, input().split()))
    S1 = 0
    S2 = sum(W)
    min_diff = S2
    for i in range(N):
        S1 += W[i]
        S2 -= W[i]
        min_diff = min(min_diff, abs(S1 - S2))
    print(min_diff)

if __name__ == '__main__':
    main()