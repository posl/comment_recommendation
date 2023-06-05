def main():
    # 获取输入
    n, k = map(int, input().split())
    t = []
    for i in range(n):
        t.append(list(map(int, input().split())))
    # 从1号城市开始，访问其他城市的所有路径
    city = [i for i in range(1, n)]
    # 计算路径总时间
    total_time = 0
    for i in range(n - 1):
        total_time += t[city[i - 1]][city[i]]
    # 计算路径总数
    total_count = 0
    while True:
        # 递增最后一个访问的城市
        city[-1] += 1
        # 最后一个访问城市超出范围，回溯
        if city[-1] >= n:
            # 没有访问城市，退出
            if len(city) == 1:
                break
            # 最后一个访问城市回到1号城市，删除最后一个访问城市，继续回溯
            elif city[-1] == 1:
                city.pop()
            # 最后一个访问城市不是1号城市，继续回溯
            else:
                continue
        # 计算路径总时间
        total_time = 0
        for i in range(n - 1):
            total_time += t[city[i - 1]][city[i]]
        # 路径总时间等于k，路径总数加1
        if total_time == k:
            total_count += 1
    # 打印答案
    print(total_count)
