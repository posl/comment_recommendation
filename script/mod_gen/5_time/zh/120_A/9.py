def main():
    # 读取输入
    a,b,c = map(int,input().split())
    # 处理
    d = b//a
    if d > c:
        d = c
    # 输出
    print(d)

if __name__ == '__main__':
    main()