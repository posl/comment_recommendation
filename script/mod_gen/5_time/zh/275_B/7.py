def cal(a,b,c,d,e,f):
    if a*b*c >= d*e*f:
        return (a*b*c)%(998244353)-(d*e*f)%(998244353)
    else:
        return (d*e*f)%(998244353)-(a*b*c)%(998244353)

if __name__ == '__main__':
    cal()