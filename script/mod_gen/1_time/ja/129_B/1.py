def main():
    N = int(input())
    W = list(map(int, input().split()))
    # N = 8
    # W = [27, 23, 76, 2, 3, 5, 62, 52]
    # N = 4
    # W = [1, 3, 1, 1]
    # N = 3
    # W = [1, 2, 3]
    # N = 2
    # W = [1, 1]
    # print(N)
    # print(W)
    S1 = 0
    S2 = 0
    diff = 0
    min_diff = 0
    for i in range(N):
        S1 = sum(W[0:i + 1])
        S2 = sum(W[i + 1:N])
        # print(S1)
        # print(S2)
        diff = abs(S1 - S2)
        if i == 0:
            min_diff = diff
        elif diff < min_diff:
            min_diff = diff
        # print(diff)
        # print(min_diff)
    print(min_diff)

if __name__ == '__main__':
    main()