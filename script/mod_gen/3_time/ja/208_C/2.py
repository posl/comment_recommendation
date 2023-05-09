def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if K <= N:
        for i in range(N):
            if i < K:
                print(K // N + 1)
            else:
                print(K // N)
    else:
        for i in range(N):
            if i < N - 1:
                print(a[i] + (K - N) // N)
            else:
                print(a[i] + (K - N) // N + (K - N) % N)
main()

if __name__ == '__main__':
    main()