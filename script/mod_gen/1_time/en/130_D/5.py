def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N - i):
            if sum(A[j:j + i + 1]) >= K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()