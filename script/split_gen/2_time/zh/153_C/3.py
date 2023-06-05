def main():
    # 读取输入
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    # 求和
    sum_a = sum(a)
    # 判断
    if h <= sum_a:
        print("Yes")
    else:
        print("No")
