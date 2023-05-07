def main():
    N = int(input())
    W = list(map(int, input().split()))
    W = [0] + W
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] + W[i]
    ans = 10**9
    for i in range(1, N):
        ans = min(ans, abs(S[N] - 2 * S[i]))
    print(ans)

if __name__ == '__main__':
    main()