def main():
    # 读入数据
    a,b,n = map(int, input().split())
    # 计算结果
    x = min(b-1,n)
    ans = (a*x)//b - a*(x//b)
    # 打印结果
    print(ans)

if __name__ == '__main__':
    main()