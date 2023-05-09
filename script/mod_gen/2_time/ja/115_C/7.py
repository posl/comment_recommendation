def main():
    #入力
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    #ソート
    h.sort()
    #各区間の最小値を求める
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, h[i + K - 1] - h[i])
    #出力
    print(ans)

if __name__ == '__main__':
    main()