def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    P = X[N // 2]
    ans = 0
    for i in range(N):
        ans += abs(X[i] - P)
    print(ans)

if __name__ == '__main__':
    main()