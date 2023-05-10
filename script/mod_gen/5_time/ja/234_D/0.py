def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K, P)
    #print(N, K, P)
    #print(sorted(P))
    #print(sorted(P)[K-1])
    #print(sorted(P)[K-1:])
    for i in range(N-K+1):
        print(sorted(P)[K-1:][i])

if __name__ == '__main__':
    main()