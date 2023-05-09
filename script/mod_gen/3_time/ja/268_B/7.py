def main():
    # 入力
    s = input()
    t = input()
    # 処理
    if t.startswith(s):
        ans = "Yes"
    else:
        ans = "No"
    # 出力
    print(ans)

if __name__ == '__main__':
    main()