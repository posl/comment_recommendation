def main():
    a,b,c,d,e,f = map(int,input().split())
    x = a*b*c
    y = d*e*f
    print((x-y)%998244353)
