def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 100000
    for T in range(1, N):
        S1 = sum(W[:T])
        S2 = sum(W[T:])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
