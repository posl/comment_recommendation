def main():
    # 读取数据
    a,b = map(int,input().split())
    # 判断
    if b%a==0:
        print(a+b)
    else:
        print(b-a)

if __name__ == '__main__':
    main()