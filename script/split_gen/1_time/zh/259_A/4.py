def main():
    #输入
    n,m,x,t,d = map(int,input().split())
    #计算
    for i in range(m,n):
        if i == x:
            t += d
        else:
            t += d
    #输出
    print(t)
