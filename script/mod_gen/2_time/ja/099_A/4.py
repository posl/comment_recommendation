def main():
    # 入力
    N = int(input())
    # 処理
    if N <= 999:
        ans = "ABC"
    else:
        ans = "ABD"
    # 出力
    print(ans)

if __name__ == '__main__':
    main()