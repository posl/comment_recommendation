def main():
    # 文字列S,Tと整数A,Bと文字列Uの入力を取得
    S,T = input().split()
    A,B = map(int, input().split())
    U = input()
    # 文字列S,TがそれぞれUと同じかどうかで条件分岐
    if S == U:
        A -= 1
    else:
        B -= 1
    # 結果を出力
    print(A,B)

if __name__ == '__main__':
    main()