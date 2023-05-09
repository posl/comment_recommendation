def main():
    # 入力
    L, R = map(int, input().split())
    s = "atcoder"
    # 出力
    print(s[L-1:R])

if __name__ == '__main__':
    main()