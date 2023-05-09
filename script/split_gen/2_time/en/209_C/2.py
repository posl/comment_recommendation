def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 1
    for i in range(N-1):
        if C[i] < C[i+1]:
            ans *= 1
        elif C[i] > C[i+1]:
            ans *= 0
        else:
            ans *= 2
        ans %= MOD
    print(ans)
