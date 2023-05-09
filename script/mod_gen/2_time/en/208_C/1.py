def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * (N + 1)
    for i in range(N):
        b[i + 1] = b[i] + a[i]
    for i in range(N):
        if K >= (N - i) * a[i] - (b[N] - b[i]):
            print(K // (N - i))
            exit()
        K -= a[i]

if __name__ == '__main__':
    main()