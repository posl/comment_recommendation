def main():
    # 读入数据
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    # 处理并输出结果
    if s == u:
        a -= 1
    elif t == u:
