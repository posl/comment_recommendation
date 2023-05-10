def main():
    N, K = map(int, input().split())
    print(100*N*(N+1)//2*K)
    return 0

if __name__ == '__main__':
    main()