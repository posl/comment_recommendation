def main():
    # A,Bを取得
    A,B = map(int, input().split())
    # 出力
    if A > 0 and B == 0:
        print("Gold")
    elif A == 0 and B > 0:
        print("Silver")
    else:
        print("Alloy")

if __name__ == '__main__':
    main()