def main():
    # 读取输入
    line = input()
    a,b,c,d,e,f,x = line.split()
    # 转换为整数
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    x = int(x)
    # 计算高桥和青木的距离
    taka = 0
    aoki = 0
    for i in range(x):
        if i % (a+c) < a:
            taka += b
        if i % (d+f) < d:
            aoki += e

if __name__ == '__main__':
    main()