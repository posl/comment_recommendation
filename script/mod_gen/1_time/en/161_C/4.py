def main():
    N, K = map(int, input().split())
    if N < K:
        print(N)
    else:
        print(N % K)

if __name__ == '__main__':
    main()