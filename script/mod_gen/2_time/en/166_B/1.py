def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [[] for _ in range(K)]
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        for j in range(d[i]):
            if A[i][j] not in A[i]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()