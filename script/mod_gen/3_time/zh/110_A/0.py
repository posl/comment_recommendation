def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 计算结果
    print(max(a+b+c, a+b*c, a*b+c, a*b*c))

if __name__ == '__main__':
    main()