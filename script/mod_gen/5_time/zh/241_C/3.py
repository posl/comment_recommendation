def solve():
    n = int(input())
    s = [list(input()) for _ in range(n)]
    # 1. 6 * 6の正方形があるかを探す
    # 2. 6 * 6の正方形がなければ、2マスを黒く塗る
    # 3. 6 * 6の正方形があれば、それを黒く塗る
    for i in range(n - 6 + 1):
        for j in range(n - 6 + 1):
            flag = True
            for k in range(6):
                for l in range(6):
                    if s[i + k][j + l] == '#':
                        flag = False
            if flag:
                print('Yes')
                return
    if n == 6:
        print('No')
        return
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                continue
            s[i][j] = '#'
            for k in range(n - 6 + 1):
                for l in range(n - 6 + 1):
                    flag = True
                    for m in range(6):
                        for o in range(6):
                            if s[k + m][l + o] == '#':
                                flag = False
                    if flag:
                        print('Yes')
                        return
            s[i][j] = '.'
    print('No')
solve()
