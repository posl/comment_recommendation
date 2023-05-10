def main():
    N, K = map(int, input().split())
    print(N%K if N>K else min(N, abs(N-K)))

if __name__ == '__main__':
    main()