def main():
    N,K = map(int,input().split())
    print( (N*(N+1)*K//2)*100 + (K*(K+1)*N//2) )

if __name__ == '__main__':
    main()