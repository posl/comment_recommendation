def main():
    # 读入数据
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    # 计算答案
    t -= 1
    t %= sum(a)
    for i in range(n):
        if t < a[i]:
            break
        t -= a[i]
    # 打印答案
    print(i + 1, t + 1)
