def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    # 计算满意度积分
    result = 0
    for i in range(n):
        result += b[a[i] - 1]
        if i < n - 1 and a[i + 1] - a[i] == 1:
            result += c[a[i] - 1]
    # 打印输出
    print(result)
