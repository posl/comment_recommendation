def main():
    # データ入力
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    # 1桁の場合
    if n == 1:
        for i in range(10):
            if i == sc[0][0] and i == sc[0][1]:
                print(i)
                exit()
        print(-1)
        exit()
    # 2桁以上の場合
    for i in range(10**(n-1), 10**n):
        # 桁数チェック
        if len(str(i)) != n:
            continue
        # 条件チェック
        for j in range(m):
            if int(str(i)[sc[j][0]-1]) != sc[j][1]:
                break
            if j == m-1:
                print(i)
                exit()
    print(-1)

if __name__ == '__main__':
    main()