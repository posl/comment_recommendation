def main():
    # 读入数据
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    # 按照村庄的位置排序
    ab.sort(key=lambda x: x[0])
    # 遍历村庄
    i = 0
    while k > 0 and i < n:
        # k - ab[i][0]是从当前村庄到下一个村庄所需的日元数
        # k - ab[i][0] < 0意味着无法到达下一个村庄
        if k - ab[i][0] < 0:
            break
        # 否则可以到达下一个村庄
        k += ab[i][1] - ab[i][0]
        i += 1
    # 输出结果
    print(k + ab[i - 1][0] if i > 0 else k)
