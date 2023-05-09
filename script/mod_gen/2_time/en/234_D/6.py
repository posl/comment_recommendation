def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K)
    #print(P)
    for i in range(K, N+1):
        #print(i)
        #print(P[i-K:i])
        print(sorted(P[i-K:i])[-2])

if __name__ == '__main__':
    main()