def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 100000000
    for i in range(N):
        S1 = sum(W[:i+1])
        S2 = sum(W[i+1:])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
