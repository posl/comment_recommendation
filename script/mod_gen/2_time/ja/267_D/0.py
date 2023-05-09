def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, sum(A[i:i + M]) + sum(range(1, M + 1)))
    print(ans)

if __name__ == '__main__':
    main()