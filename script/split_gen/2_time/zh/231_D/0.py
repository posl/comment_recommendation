def solve():
    # 读取输入
    n, m = map(int, input().split())
    # 用来记录每个人的左右边界
    l, r = [0] * n, [0] * n
    # 用来记录每个人的右边界的最小值和左边界的最大值
    min_right, max_left = n, 0
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        # 更新左右边界
        l[b] = max(l[b], a + 1)
        r[a] = max(r[a], b + 1)
        # 更新右边界的最小值和左边界的最大值
        min_right = min(min_right, b)
        max_left = max(max_left, a)
    # 用来记录当前人的左边界的最大值
    max_l = 0
    for i in range(n):
        # 更新当前人的左边界的最大值
        max_l = max(max_l, l[i])
        # 如果当前人的左边界的最大值大于右边界的最小值，说明不满足条件
        if max_l > min_right:
            print("No")
            return
        # 如果当前人的右边界的最小值大于左边界的最大值，说明不满足条件
        if r[i] > max_left:
            print("No")
            return
    print("Yes")
