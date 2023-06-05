def main():
    N,K = map(int, input().split())
    x = list(map(int, input().split()))
    #print(N,K,x)
    if K == 1:
        print(0)
    else:
        #print(x)
        #print(x[K-1])
        #print(x[0])
        #print(x[K-1] - x[0])
        #print(x[N-1] - x[K])
        print(min(x[K-1] - x[0], x[N-1] - x[K]))
main()
