def solve():
    A, B, C, D = map(int, input().split())
    # 操作回数
    n = 0
    # 水色のボールの個数
    s = A
    # 赤色のボールの個数
    r = 0
    while s > r * D:
        if s <= r * D:
            break
        s += B
        r += C
        n += 1
    if s <= r * D:
        print(n)
    else:
        print(-1)

if __name__ == '__main__':
    solve()