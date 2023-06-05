def main():
    # 输入
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    # 处理
    min_diff = 1000000
    min_index = 0
    for i in range(n):
        diff = abs(a - (t - h[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            min_index = i + 1
    # 输出
    print(min_index)
