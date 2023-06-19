def main():
    # 读取A,B,C
    a, b, c = map(int, input().split())
    # 通过穷举法找出最大值
    max = 0
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                # 通过这种方法将三个数字排列成一个三位数
                num = i * 100 + j * 10 + k
                # 如果num小于等于C，则直接跳过
                if num <= c:
                    continue
                # 如果num小于等于B，则直接跳过
                if num <= b:
                    continue
                # 如果num小于等于A，则直接跳过
                if num <= a:
                    continue
                # 如果num大于max，则将num赋值给max
                if num > max:
                    max = num
    # 打印结果
    print(max)

if __name__ == '__main__':
    main()