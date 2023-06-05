def main():
    import sys
    import math
    # 获取输入
    input_line = sys.stdin.readline()
    # 分割输入
    input_line = input_line.split()
    # 转化为整数
    input_line = [int(i) for i in input_line]
    # 计算
    area = input_line[0] * input_line[1] / 2
    # 输出
    print(int(area))

if __name__ == '__main__':
    main()