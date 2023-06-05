def main():
    # 读取数据
    r, c = map(int, input().split())
    # 逻辑处理
    if (r + c) % 2 == 0:
        print("黑色")
    else:
        print("白色")
    # 输出结果

if __name__ == '__main__':
    main()