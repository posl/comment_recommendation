def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 从第一个角开始旋转
    ans = 0
    for i in range(n):
        # 记录角度
        deg = 0
        for j in range(n):
            # 每次旋转角度
            if i != j:
                # 逆时针旋转
                x = a[j] - a[i]
                if x < 0:
                    x += 360
                deg = max(deg, x)
        # 记录最大角度
        ans = max(ans, deg)
    # 输出
    print(ans)
