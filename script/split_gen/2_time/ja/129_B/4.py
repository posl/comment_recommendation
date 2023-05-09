def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 10**9
    for i in range(1, N):
        S1 = sum(W[:i])
        S2 = sum(W[i:])
        ans = min(ans, abs(S1-S2))
    print(ans)
