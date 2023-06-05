def main():
    # 读取输入
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    # 排序
    x.sort()
    # 计算棋子间距
    distance = [0] * (m - 1)
    for i in range(m - 1):
        distance[i] = x[i + 1] - x[i]
    # 排序
    distance.sort()
    # 计算差值
    ans = 0
    for i in range(m - n):
        ans += distance[i]
    # 输出
    print(ans)
