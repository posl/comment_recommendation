def main():
    # 入力
    L = int(input())
    # 処理
    if L % 3 == 0:
        ans = (L / 3) ** 3
    else:
        ans = (L // 3) ** 3
        ans = max(ans, (L // 3 + 1) ** 3)
        ans = max(ans, (L // 3) ** 3 * (L % 3))
        ans = max(ans, (L // 3 + 1) ** 3 * (L % 3))
    # 出力
    print(ans)

if __name__ == '__main__':
    main()