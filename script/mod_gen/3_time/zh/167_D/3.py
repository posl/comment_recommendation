def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 记录访问过的城市
    visited = [0] * n
    # 记录访问过的城市的顺序
    visited_order = []
    # 访问的城市
    city = 0
    # 访问的城市的顺序
    order = 1
    # 访问城市
    visited[city] = order
    visited_order.append(city)
    # 访问次数
    count = 1
    # 访问下一个城市
    city = a[city] - 1
    while True:
        # 如果访问过
        if visited[city] != 0:
            # 记录访问次数
            count = count - visited[city] + 1
            # 记录访问的城市的顺序
            visited_order = visited_order[visited[city] - 1:]
            break
        # 记录访问的城市
        visited[city] = order + 1
        visited_order.append(city)
        # 访问次数加一
        count += 1
        # 访问下一个城市
        city = a[city] - 1
        # 增加访问的城市的顺序
        order += 1
    # 访问次数取模
    k = k % count
    # 访问的城市的顺序
    visited_order = visited_order[:k]
    # 访问的城市
    city = visited_order[-1]
    # 访问次数
    count = len(visited_order)
    # 访问下一个城市
    city = a[city] - 1
    while True:
        # 访问次数加一
        count += 1
        # 访问下一个城市
        city = a[city] - 1
        # 如果访问过
        if city in visited_order:
            # 访问的城市的顺序
            visited

if __name__ == '__main__':
    main()