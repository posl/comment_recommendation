def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**10
    # N-K+1 個の区間について考える
    for i in range(N-K+1):
        # 区間の左端のろうそくに火を付けるときの最小の時間
        left = abs(X[i]) + abs(X[i]-X[i+K-1])
        # 区間の右端のろうそくに火を付けるときの最小の時間
        right = abs(X[i+K-1]) + abs(X[i]-X[i+K-1])
        # どちらかの時間が最小のものを答えにする
        ans = min(ans, left, right)
    print(ans)

if __name__ == '__main__':
    main()