def main():
    N, K = map(int, input().split())
    print(min(N % K, K - N % K))

if __name__ == '__main__':
    main()