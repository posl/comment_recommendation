def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    if (N-1)%(K-1)==0:
        print((N-1)//(K-1))
    else:
        print((N-1)//(K-1)+1)

if __name__ == '__main__':
    main()