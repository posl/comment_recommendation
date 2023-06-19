def main():
    # 读入数据
    X, Y, R = map(float, input().split())
    # 计算圆内网格点的数量
    ans = 0
    for x in range(int(X - R), int(X + R) + 1):
        for y in range(int(Y - R), int(Y + R) + 1):
            if (X - x) ** 2 + (Y - y) ** 2 <= R ** 2:
                ans += 1
    # 输出答案
    print(ans)
