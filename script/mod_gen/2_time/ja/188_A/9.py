def main():
    # 標準入力から得点を取得する
    x, y = map(int, input().split())
    # 優勢側の得点を求める
    if x < y:
        a = x
    else:
        a = y
    # 劣勢側の得点を求める
    if x < y:
        b = y
    else:
        b = x
    # 劣勢側が3点を取った場合の得点を求める
    c = b + 3
    # 優勢側の得点より劣勢側の得点が高い場合はYes
    if a < c:
        print("Yes")
    # 優勢側の得点より劣勢側の得点が高い場合はNo
    else:
        print("No")

if __name__ == '__main__':
    main()