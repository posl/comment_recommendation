def main():
    # 读入数据
    R, X, Y = input().split()
    R = int(R)
    X = int(X)
    Y = int(Y)
    # 计算结果
    ans = 0
    # 1.求出从原点到目标点的距离
    dist = (X ** 2 + Y ** 2) ** 0.5
    # 2.用距离除以R，得到步数
    ans = dist // R
    # 3.判断是否有余数
    if dist % R != 0:
        ans += 1
    # 4.如果步数为1，且余数不为0，则步数加1
    if ans == 1 and dist % R != 0:
        ans += 1
    # 5.输出结果
    print(int(ans))

if __name__ == '__main__':
    main()