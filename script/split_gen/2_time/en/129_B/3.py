def main():
    N = int(input())
    W = list(map(int, input().split()))
    S1 = 0
    S2 = sum(W)
    min_diff = float('inf')
    for i in range(1, N):
        S1 += W[i-1]
        S2 -= W[i-1]
        min_diff = min(min_diff, abs(S1 - S2))
    print(min_diff)
