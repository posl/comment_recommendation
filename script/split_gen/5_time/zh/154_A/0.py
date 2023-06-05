def main():
    # 读入数据
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    # 处理数据
    if u == s:
        a -= 1
    else:
        b -= 1
    # 输出结果
    print(a, b)
