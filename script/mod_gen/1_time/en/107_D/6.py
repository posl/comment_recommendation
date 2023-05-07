def main():
    N = int(input())
    A = list(map(int, input().split()))
    p = [0] * (N + 1)
    for i in range(1, N + 1):
        p[i] = p[i - 1] + A[i - 1]
    ans = 0
    for i in range(N):
        ans += (N - i) * A[i] - (p[N] - p[i])
    print(ans / N)

if __name__ == '__main__':
    main()