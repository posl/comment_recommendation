def main():
    # 读取数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 一开始的镇
    start = 1
    # 从第一次开始循环
    for i in range(k):
        start = a[start - 1]
    # 输出结果
    print(start)
