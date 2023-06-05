def main():
    # 读取数据
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    # 按照村庄编号升序排序
    ab.sort()
    # 计算最后一村的编号
    village = 0
    for a, b in ab:
        if k < a - village:
            break
        k += b - (a - village)
        village = a
    # 输出结果
    print(village + k)
