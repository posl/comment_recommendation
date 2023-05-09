def main():
    # 標準入力から値を取得する
    p, q, r = map(int, input().split())
    # 飛行時間の和の最小値を出力
    print(min(p+q, q+r, r+p))

if __name__ == '__main__':
    main()