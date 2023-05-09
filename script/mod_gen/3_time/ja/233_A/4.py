def main():
    #入力
    X, Y = map(int, input().split())
    #計算
    ans = 0
    if Y % 10 != 0:
        ans = (Y // 10 + 1) * 10 - X
    else:
        ans = Y - X
    #出力
    print(ans)

if __name__ == '__main__':
    main()