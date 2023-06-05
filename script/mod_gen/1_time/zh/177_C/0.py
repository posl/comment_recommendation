def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    N = 4
    A = [141421356, 17320508, 22360679, 244949]
    # A = [1,2,3]
    mod = 10**9 + 7
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            ans += A[i] * A[j]
            ans %= mod
    print(ans)

if __name__ == '__main__':
    main()