def main():
    # input
    N = int(input())
    W = list(map(int,input().split()))
    # processing
    W_sum = sum(W)
    S_1 = 0
    S_2 = W_sum
    min_diff = W_sum
    for i in range(N):
        S_1 += W[i]
        S_2 -= W[i]
        diff = abs(S_1 - S_2)
        if diff < min_diff:
            min_diff = diff
    # output
    print(min_diff)

if __name__ == '__main__':
    main()