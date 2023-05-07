def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M - sum(A) > K:
        print(-1)
    else:
        print(max(0, N * M - sum(A)))
main()

if __name__ == '__main__':
    main()