def main():
    N = int(input())
    W = [int(x) for x in input().split()]
    S1 = 0
    S2 = sum(W)
    min_diff = 10000
    for i in range(1,N):
        S1 += W[i-1]
        S2 -= W[i-1]
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()