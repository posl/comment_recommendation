def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = 0
    for i in range(N - 1):
        ans += A[i] * (N - i - 1)
    print(ans - S[N - 1])

if __name__ == '__main__':
    main()