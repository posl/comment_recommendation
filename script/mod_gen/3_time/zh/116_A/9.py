def main():
    # 读取输入
    s = input()
    # 用空格分割输入，得到字符串数组
    s = s.split()
    # 将字符串数组转换为整数数组
    s = [int(x) for x in s]
    # 计算面积
    area = s[0] * s[1] // 2
    # 输出结果
    print(area)

if __name__ == '__main__':
    main()