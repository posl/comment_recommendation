def main():
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    S1 = 0
    S2 = S
    for t in range(N):
        S1 += W[t]
        S2 -= W[t]
        if abs(S1-S2) > abs(S1-W[t]-S2+W[t]):
            S1 -= W[t]
            S2 += W[t]
    print(abs(S1-S2))
