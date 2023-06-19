def main():
    # 读取输入
    a, b, c, k = map(int, input().split())
    # 可以用a张1的卡片
    if k <= a:
        print(k)
        return
    # 可以用a+b张卡片
    if k <= a + b:
        print(a)
        return
    # 其他情况
    print(a - (k - a - b))
