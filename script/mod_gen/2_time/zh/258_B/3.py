def main():
    # 读取输入
    k = int(input())
    # 计算结果
    h = k // 60
    m = k % 60
    # 输出
    print("{:02d}:{:02d}".format(h+21, m))

if __name__ == '__main__':
    main()