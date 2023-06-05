def main():
    # 输入
    k = int(input())
    # 生成数列
    i = 0
    n = 1
    while i < k:
        n += 1
        if is_02(n):
            i += 1
    # 输出
    print(n)
