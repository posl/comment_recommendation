def main():
    # 读入数据
    n = int(input())
    s = list(map(int, input().split()))
    # 计算答案
    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    # 打印答案
    print(' '.join(map(str, a)))
