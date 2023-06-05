def main():
    # 读取输入
    a,b,c = map(int,input().split())
    # 判断
    if a>b and a>c:
        print(a+b)
    elif b>a and b>c:
        print(b+c)
    else:
        print(c+a)

if __name__ == '__main__':
    main()