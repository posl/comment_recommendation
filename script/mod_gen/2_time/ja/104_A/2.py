def main():
    #入力
    R = int(input())
    #出力
    if R < 1200:
        print("ABC")
    elif R < 2800:
        print("ARC")
    else:
        print("AGC")

if __name__ == '__main__':
    main()