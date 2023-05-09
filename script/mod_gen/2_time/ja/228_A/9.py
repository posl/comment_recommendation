def main():
    S, T, X = map(int, input().split())
    # 12:30 = 30分
    # 電気がついている時間を計算
    if S > T:
        t = 24 - S + T
    else:
        t = T - S
    # 12:30 に電気がついているかどうか
    if X + 0.5 >= S and X + 0.5 < T:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()