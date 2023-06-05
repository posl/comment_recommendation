def main():
    #读取输入
    line = input()
    #拆分输入
    a, b = line.split()
    #计算
    sum_a = int(a[0]) + int(a[1]) + int(a[2])
    sum_b = int(b[0]) + int(b[1]) + int(b[2])
    #比较
    if sum_a > sum_b:
        print(sum_a)
    else:
        print(sum_b)

if __name__ == '__main__':
    main()