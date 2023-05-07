def main():
    N, K = map(int, input().split())
    print((N-K+2)*(K-1) % (10**9+7))

if __name__ == '__main__':
    main()