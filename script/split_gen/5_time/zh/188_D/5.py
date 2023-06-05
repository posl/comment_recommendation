def main():
    N, C = map(int, input().split())
    A, B, C = [], [], []
    for _ in range(N):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    # 1. 按照开始时间排序
    # 2. 合并时间段
    # 3. 遍历时间段，计算总费用
    # 4. 比较总费用和C，取最小值
    # 5. 如果最小值小于C，输出最小值；否则输出C
    # 6. 如果没有合并时间段，输出总费用
    # 1. 按照开始时间排序
    AB = sorted(zip(A, B, C), key=lambda x: x[0])
    # 2. 合并时间段
    AB = merge(AB)
    # 3. 遍历时间段，计算总费用
    cost = 0
    for a, b, c in AB:
        cost += c * (b - a + 1)
    # 4. 比较总费用和C，取最小值
    cost = min(cost, C)
    # 5. 如果最小值小于C，输出最小值；否则输出C
    print(cost)
