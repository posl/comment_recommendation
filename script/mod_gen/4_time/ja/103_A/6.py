def main():
    # データ入力
    a = list(map(int, input().split()))
    # 処理
    # ソート
    a.sort()
    # 出力
    print(a[2] - a[0])

if __name__ == '__main__':
    main()