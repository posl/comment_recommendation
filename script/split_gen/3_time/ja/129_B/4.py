def main():
    N = int(input())
    W = list(map(int, input().split()))
    S1 = 0
    S2 = sum(W)
    min_diff = 1000000
    for T in range(1, N):
        S1 += W[T-1]
        S2 -= W[T-1]
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
