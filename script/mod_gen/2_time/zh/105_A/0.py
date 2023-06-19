def main():
    N, K = map(int, input().split())
    if N <= K:
        print(0)
    else:
        print(N - K)

if __name__ == '__main__':
    main()