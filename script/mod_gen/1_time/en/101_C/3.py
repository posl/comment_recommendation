def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    if (N-K)%(K-1)==0:
        print((N-K)//(K-1)+1)
    else:
        print((N-K)//(K-1)+2)

if __name__ == '__main__':
    main()