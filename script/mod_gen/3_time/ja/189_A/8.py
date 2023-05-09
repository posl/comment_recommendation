def main():
    # 入力
    c1,c2,c3 = input().split()
    # 出力
    if c1==c2 and c2==c3:
        print("Won")
    else:
        print("Lost")

if __name__ == '__main__':
    main()