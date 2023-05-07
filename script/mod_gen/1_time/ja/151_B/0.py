def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M <= sum(A):
        print(0)
    elif N * M - sum(A) <= K:
        print(N * M - sum(A))
    else:
        print(-1)

if __name__ == '__main__':
    main()