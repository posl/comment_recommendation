def main():
    N = int(input())
    W = [int(w) for w in input().split()]
    S1 = 0
    S2 = sum(W)
    min_diff = 10**6
    for i in range(N-1):
        S1 += W[i]
        S2 -= W[i]
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()