def main():
    # 从标准输入读取
    a,b,c = map(int, input().split())
    # 从瓶子2转移到瓶子1
    b = b + c
    # 2号瓶中还有多少水
    c = 0
    # 1号瓶中还可以装多少水
    a = a - b
    # 1号瓶中装满
    if a < 0:
        c = abs(a)
        a = 0
    print(c)

if __name__ == '__main__':
    main()