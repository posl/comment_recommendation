def main():
    # 入力
    s = input()
    # 753 との差の最小値を求める
    ans = 10 ** 9
    for i in range(len(s) - 2):
        x = int(s[i:i + 3])
        ans = min(ans, abs(x - 753))
    # 出力
    print(ans)

if __name__ == '__main__':
    main()