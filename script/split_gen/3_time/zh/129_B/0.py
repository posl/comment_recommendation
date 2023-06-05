def main():
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    ans = S
    S1 = 0
    for i in range(N):
        S1 += W[i]
        S2 = S - S1
        ans = min(ans, abs(S1 - S2))
    print(ans)
