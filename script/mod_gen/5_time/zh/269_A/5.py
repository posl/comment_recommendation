def main():
    # 读取a,b,c,d
    a, b, c, d = map(int,input().split())
    # 计算(a+b)*(c-d)
    result = (a + b) * (c - d)
    # 输出结果
    print(result)
    # 输出Takahashi
    print("Takahashi")

if __name__ == '__main__':
    main()