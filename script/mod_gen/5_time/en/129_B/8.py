def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 100000000000000
    for i in range(1, N):
        S1 = sum(W[:i])
        S2 = sum(W[i:])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()