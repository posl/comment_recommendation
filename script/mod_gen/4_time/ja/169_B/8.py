def main():
    # データ入力
    N = int(input())
    A = list(map(int, input().split()))
    # 処理
    # 0があれば0を出力
    if 0 in A:
        print(0)
        return
    # それ以外は積を出力
    ans = 1
    for a in A:
        ans *= a
        if ans > 10**18:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()