def main():
    # 入力
    S = input()
    # 8の倍数を作れるかどうか
    flag = False
    # 8の倍数を作れるかどうか判定
    if "8" in S:
        flag = True
    elif "0" in S:
        flag = True
    elif "7" in S:
        flag = True
    elif "6" in S:
        flag = True
    elif "5" in S:
        flag = True
    elif "4" in S:
        flag = True
    elif "3" in S:
        flag = True
    elif "2" in S:
        flag = True
    elif "1" in S:
        flag = True
    else:
        flag = False
    # 出力
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()