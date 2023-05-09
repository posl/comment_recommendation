def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    if K >= N:
        ans = [K//N] * N
        K = K % N
    for i in range(K):
        ans[A.index(A[i])] += 1
    print(*ans, sep='
')

if __name__ == '__main__':
    main()