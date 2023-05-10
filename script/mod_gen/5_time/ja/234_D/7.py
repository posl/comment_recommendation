def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K)
    #print(P)
    #print(sorted(P))
    #print(sorted(P)[K-1:N])
    for i in range(K, N+1):
        print(sorted(P)[K-1:N][i-K])

if __name__ == '__main__':
    main()