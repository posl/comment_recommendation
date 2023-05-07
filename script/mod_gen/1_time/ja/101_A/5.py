def main():
    # 入力
    S = input()
    # 処理
    ans = 0
    for i in S:
        if i == "+":
            ans += 1
        else:
            ans -= 1
    # 出力
    print(ans)

if __name__ == '__main__':
    main()