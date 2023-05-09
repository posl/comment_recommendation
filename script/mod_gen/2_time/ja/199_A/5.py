def main():
    #標準入力から A B C を取得
    A, B, C = map(int, input().split())
    #A^2 + B^2 < C^2 かを判定して Yes または No を出力
    if A**2 + B**2 < C**2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()