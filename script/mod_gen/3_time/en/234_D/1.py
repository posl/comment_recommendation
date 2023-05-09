def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    for i in range(K, N):
        print(P[i - K])
    for i in range(K):
        print(P[N - K])

if __name__ == '__main__':
    main()