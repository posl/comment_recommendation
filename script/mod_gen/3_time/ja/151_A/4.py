def main():
    #入力
    C = input()
    #処理
    #ord()は文字のアスキーコードを返す関数
    #chr()はアスキーコードを文字に変換する関数
    ans = chr(ord(C) + 1)
    #出力
    print(ans)

if __name__ == '__main__':
    main()