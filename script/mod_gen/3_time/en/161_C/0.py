def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(min(N % K, abs(N % K - K)))

if __name__ == '__main__':
    main()