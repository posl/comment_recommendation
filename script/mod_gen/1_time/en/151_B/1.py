def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(max(0, N * M - sum(A)))

if __name__ == '__main__':
    main()