def main():
    # 读取输入
    a,b,c,d,e,f = map(int, input().split())
    # 计算结果
    result = a*b*c - d*e*f
    # 打印结果
    print(result%998244353)

if __name__ == '__main__':
    main()