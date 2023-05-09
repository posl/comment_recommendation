def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = 10 ** 18
    for i in range(N - 2):
        a = S[i + 1]
        b = S[N] - S[i + 1]
        c = abs(a - b)
        ans = min(ans, c)
    for i in range(N - 1):
        a = S[i + 1]
        b = S[N] - S[i + 1]
        c = abs(a - b)
        ans = min(ans, c)
    print(ans)
main()

if __name__ == '__main__':
    main()