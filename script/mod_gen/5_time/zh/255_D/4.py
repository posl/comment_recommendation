def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort(reverse=True)
    X.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += abs(A[i] - X[i])
    print(ans)

if __name__ == '__main__':
    main()