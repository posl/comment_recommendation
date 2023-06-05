def main():
    # 读入数据
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    # 从左上角开始，向右下方向走，求和
    # 从右下角开始，向左上方向走，求和
    # 两个和相加，减去中间重复计算的值
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += int(a[0][i])
        sum1 += int(a[i][0])
        sum2 += int(a[n-1][i])
        sum2 += int(a[i][n-1])
    sum1 -= int(a[0][0])
    sum1 -= int(a[n-1][n-1])
    print(sum1 + sum2)

if __name__ == '__main__':
    main()