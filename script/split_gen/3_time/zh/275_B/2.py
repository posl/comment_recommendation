def main():
    #读取输入
    a,b,c,d,e,f = map(int,input().split())
    #计算结果
    ans = (a*b*c-d*e*f)%998244353
    #输出结果
    print(ans)
