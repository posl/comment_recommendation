def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print((N-1+K-2)//(K-1))

if __name__ == '__main__':
    main()