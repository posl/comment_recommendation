def main():
    # 读取输入
    n, q = map(int, input().split())
    s = input()
    # 处理
    for i in range(q):
        # 读取输入
        t, x = map(int, input().split())
        if t == 2:
            # 输出
            print(s[x - 1])
        else:
            # 处理
            s = s[-x:] + s[:-x]
