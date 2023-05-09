def main():
    N = int(input())
    W = list(map(int, input().split()))
    S1 = W[0]
    S2 = sum(W[1:])
    ans = abs(S1 - S2)
    for i in range(1, N - 1):
        S1 += W[i]
        S2 -= W[i]
        ans = min(ans, abs(S1 - S2))
    print(ans)
