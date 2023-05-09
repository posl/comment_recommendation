def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    takahashi = 0
    aoki = 0
    for i in range(K):
        if i == 0:
            takahashi = A[i] - 1
        elif i == K-1:
            takahashi = max(takahashi, N - A[i-1])
        else:
            takahashi = max(takahashi, A[i] - A[i-1])
    print(takahashi)

if __name__ == '__main__':
    main()