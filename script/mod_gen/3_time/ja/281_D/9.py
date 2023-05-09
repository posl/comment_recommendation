def main():
    #input
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    #compute
    #output
    if K*D>N:
        print(-1)
    else:
        print(D*(sum(A[:K*D])-sum(A[:K*(D-1)])))
    return

if __name__ == '__main__':
    main()