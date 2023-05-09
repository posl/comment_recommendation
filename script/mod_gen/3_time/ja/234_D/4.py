def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K)
    #print(P)
    for i in range(K, N+1):
        #print(i)
        #print(P[0:i])
        #print(sorted(P[0:i]))
        print(sorted(P[0:i])[K-1])

if __name__ == '__main__':
    main()