def main():
    # 读取输入
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    # 排序
    p.sort()
    # 输出
    print(sum(p[:k]))
