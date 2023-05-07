def main():
    # 入力
    D, T, S = map(int, input().split())
    # ここに処理を書く
    if D <= S*T:
        print("Yes")
    else:
        print("No")
    # 出力
    #print()

if __name__ == '__main__':
    main()