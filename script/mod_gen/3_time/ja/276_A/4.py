def main():
    #入力
    s = input()
    #S に a が現れるならば最後に現れるのが何文字目かを出力し、現れないならば -1 を出力してください。
    #S は英小文字からなる長さ 1 以上 100 以下の文字列
    if "a" in s:
        print(s.rfind("a") + 1)
    else:
        print(-1)

if __name__ == '__main__':
    main()