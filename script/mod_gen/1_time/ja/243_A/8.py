def main():
    #入力
    V,A,B,C = map(int,input().split())
    #出力
    if V%A == 0:
        print("F")
    elif V%B == 0:
        print("M")
    elif V%C == 0:
        print("T")
main()

if __name__ == '__main__':
    main()