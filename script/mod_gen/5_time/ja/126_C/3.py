def main():
    N, K = map(int, input().split())
    if K == 1:
        print(1)
        return
    if N >= K:
        print((K-1)/N)
        return
    else:
        print(((N-K+1)*2 + (K-1))/N**2)

if __name__ == '__main__':
    main()