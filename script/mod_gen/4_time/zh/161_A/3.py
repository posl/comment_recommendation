def main():
    #输入
    x, y, z = map(int, input().split())
    #处理
    a = x
    b = y
    c = z
    x = c
    y = a
    z = b
    #输出
    print(x, y, z)

if __name__ == '__main__':
    main()