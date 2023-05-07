def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - K + 1):
        ans += 1
        for j in range(K):
            A[i + j] = 0
    print(ans)

if __name__ == '__main__':
    main()