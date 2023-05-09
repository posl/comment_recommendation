def main():
    N = int(input())
    C = list(map(int, input().split()))
    mod = 10**9+7
    ans = 1
    for i in range(N):
        if i == 0:
            ans *= C[i]
            ans %= mod
            continue
        if C[i] == C[i-1]:
            ans *= C[i] - 1
            ans %= mod
            continue
        if C[i] < C[i-1]:
            ans *= 0
            ans %= mod
            continue
        if C[i] > C[i-1]:
            ans *= C[i] - 1
            ans %= mod
            continue
    print(ans)
