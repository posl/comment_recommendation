def main():
    # 读取输入
    a,b,c,d,e,f,x = map(int,input().split())
    # 计算高桥和青木的行进距离
    qiao = 0
    ao = 0
    while x > 0:
        if x > a:
            qiao += a * b
            x -= a
        else:
            qiao += x * b
            x = 0
        if x > c:
            x -= c
        else:
            x = 0
        if x > d:
            ao += d * e
            x -= d
        else:
            ao += x * e
            x = 0
        if x > f:
            x -= f
        else:
            x = 0
    # 比较距离
    if qiao > ao:
        print('高桥')
    elif qiao < ao:
        print('青木')
    else:
        print('画')

if __name__ == '__main__':
    main()