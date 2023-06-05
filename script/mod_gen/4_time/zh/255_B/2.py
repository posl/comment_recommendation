def main():
    # 读入数据
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(n):
        xx,yy = map(int,input().split())
        x.append(xx)
        y.append(yy)
    # 计算最小值
    ans = 0
    for i in range(n):
        if i+1 in a:
            continue
        tmp = (x[i]**2+y[i]**2)**(1/2)
        if tmp > ans:
            ans = tmp
    print(ans)

if __name__ == '__main__':
    main()