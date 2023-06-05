def solve():
    # 读取输入
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    # 计算结果
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ok = True
            for k in range(m):
                if s[i][k] == 'x' and s[j][k] == 'x':
                    ok = False
            if ok:
                ans += 1
    # 输出结果
    print(ans)
