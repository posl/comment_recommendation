def calc(R, C, H, W):
    ans = 0
    # 上
    if R > 1:
        ans += 1
    # 下
    if R < H:
        ans += 1
    # 左
    if C > 1:
        ans += 1
    # 右
    if C < W:
        ans += 1
    return ans
