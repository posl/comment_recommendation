def main():
    # 获取输入
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    # 处理
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    # 输出
    print(count)
