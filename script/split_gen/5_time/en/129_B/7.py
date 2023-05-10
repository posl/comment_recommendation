def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 10000
    for i in range(0, N):
        S1 = sum(W[0:i+1])
        S2 = sum(W[i+1:N])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
