def main():
    #获取输入
    n,a,x,y = map(int,input().split())
    #计算结果
    if n <= a:
        ans = n * x
    else:
        ans = a * x + (n-a) * y
    #输出结果
    print(ans)
