def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if K >= N:
        print(1)
        for i in range(N-1):
            print(1)
        return
    # まずはKを配る
    for i in range(K):
        print(a[i])
    # あまりを配る
    for i in range(K, N):
        print(a[K-1])

if __name__ == '__main__':
    main()