def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**18
    for i in range(N-K+1):
        # 左に移動
        left = X[i]
        # 右に移動
        right = X[i+K-1]
        # 0 から左に移動
        if left >= 0:
            ans = min(ans, right)
        # 0 から右に移動
        elif right <= 0:
            ans = min(ans, -left)
        # 0 から左右に移動
        else:
            ans = min(ans, min(abs(left), abs(right)) + right - left)
    print(ans)

if __name__ == '__main__':
    main()