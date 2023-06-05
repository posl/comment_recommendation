def solve():
    # 读取输入
    a1, a2, a3, a4 = map(int, input().split())
    # 处理
    ans = 0
    if a1 == 100:
        ans += 1
    if a2 == 100:
        ans += 1
    if a3 == 100:
        ans += 1
    if a4 == 100:
        ans += 1
    # 输出结果
    print(ans)

if __name__ == '__main__':
    solve()