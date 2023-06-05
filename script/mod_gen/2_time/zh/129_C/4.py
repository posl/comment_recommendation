def get_min_diff():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 10000
    for t in range(1, N):
        S1 = sum(W[:t])
        S2 = sum(W[t:])
        min_diff = min(min_diff, abs(S1 - S2))
    return min_diff

if __name__ == '__main__':
    get_min_diff()