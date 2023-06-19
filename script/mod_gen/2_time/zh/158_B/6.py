def main():
    # 读取标准输入
    n, a, b = map(int, input().split())
    #计算蓝球数量
    blue = (n // (a + b)) * a
    blue += min(a, n % (a + b))
    #打印输出
    print(blue)

if __name__ == '__main__':
    main()