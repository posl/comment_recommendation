def solve(a, b):
    # 两座塔之间的距离
    distance = b - a
    # 雪覆盖的深度
    depth = 0
    # 从1开始，逐个增加雪覆盖深度，直到满足条件
    for i in range(1, distance+1):
        depth += i
        if depth >= distance:
            break
    return depth - distance

if __name__ == '__main__':
    solve()