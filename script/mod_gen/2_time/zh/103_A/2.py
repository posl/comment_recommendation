def main():
    # 读取输入
    a = list(map(int, input().split()))
    # 计算最小成本
    a.sort()
    print(a[2] - a[0])

if __name__ == '__main__':
    main()