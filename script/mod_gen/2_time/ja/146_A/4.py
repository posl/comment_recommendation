def main():
    # 文字列の入力
    s = input()
    # 出力
    if s == "SUN":
        print(7)
    elif s == "MON":
        print(6)
    elif s == "TUE":
        print(5)
    elif s == "WED":
        print(4)
    elif s == "THU":
        print(3)
    elif s == "FRI":
        print(2)
    elif s == "SAT":
        print(1)
    else:
        print("Error")

if __name__ == '__main__':
    main()