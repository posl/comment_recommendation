def main():
    N, K = map(int, input().split())
    #print(N, K)
    if K == 1:
        print(1)
        return
    if N >= K:
        print((N-K+1)/N)
        return
    else:
        #print((N-K+1)/N)
        #print(1/N)
        #print(1/K)
        print((N-K+1)/N + (1/N)*(1/2)*(K-N) + (1/N)*(1/2)*(N-1))
        return

if __name__ == '__main__':
    main()