def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    # 1. 从左到右遍历，记录每个颜色出现的次数
    # 2. 从左到右遍历，记录每个连续K个糖果的颜色数目
    # 3. 取最大值
    color = {}
    for i in range(N):
        if c[i] in color:
            color[c[i]] += 1
        else:
            color[c[i]] = 1
    # print(color)
    max_color = max(color.values())
    # print(max_color)
    color = {}
    for i in range(K):
        if c[i] in color:
            color[c[i]] += 1
        else:
            color[c[i]] = 1
    # print(color)
    max_color = max(max_color, len(color))
    # print(max_color)
    for i in range(K, N):
        if c[i-K] in color:
            color[c[i-K]] -= 1
            if color[c[i-K]] == 0:
                del color[c[i-K]]
        if c[i] in color:
            color[c[i]] += 1
        else:
            color[c[i]] = 1
        # print(color)
        max_color = max(max_color, len(color))
        # print(max_color)
    print(max_color)
