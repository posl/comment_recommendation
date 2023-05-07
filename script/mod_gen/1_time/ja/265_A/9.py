def main():
    x, y, n = map(int, input().split())
    # ループの回数
    loop = n // 3
    # 余り
    mod = n % 3
    # 答え
    ans = 0
    # 3個買う場合
    if mod == 0:
        ans = loop * y
    # 1個買う場合
    elif mod == 1:
        ans = loop * y + x
    # 2個買う場合
    else:
        ans = loop * y + x * 2
    print(ans)

if __name__ == '__main__':
    main()