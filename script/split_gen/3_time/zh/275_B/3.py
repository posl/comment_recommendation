def main():
    a,b,c,d,e,f = map(int,input().split())
    if a*b*c >= d*e*f:
        x = (a*b*c)%(998244353)
        y = (d*e*f)%(998244353)
        print(x-y)
    else:
        print("输入不符合要求")
