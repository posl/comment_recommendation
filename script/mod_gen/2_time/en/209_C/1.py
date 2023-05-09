def main():
    import sys
    input = sys.stdin.readline
    mod = 10**9 + 7
    N = int(input())
    C = list(map(int, input().split()))
    if C[0] == 1:
        ans = 1
    else:
        ans = 0
    for i in range(1, N):
        if C[i] < C[i-1]:
            ans = 0
            break
        elif C[i] == C[i-1]:
            ans *= 2
        elif C[i] - C[i-1] == 1:
            ans *= C[i-1]
        else:
            ans *= C[i-1] * (C[i] - C[i-1] + 1)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()