def main():
    # 入力
    x1, y1, x2, y2 = map(int, input().split())
    # 処理
    # x1, y1, x2, y2の差が等しい時
    if x1 - x2 == y1 - y2:
        ans = "Yes"
    # x1, y1, x2, y2の和が等しい時
    elif x1 + y1 == x2 + y2:
        ans = "Yes"
    else:
        ans = "No"
    # 出力
    print(ans)

if __name__ == '__main__':
    main()