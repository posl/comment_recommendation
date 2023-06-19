def main():
    # 读入数据
    a,b,n=map(int,input().split())
    # 计算结果
    x=min(n,b-1)
    ans=a*x//b-a*(x//b)
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()