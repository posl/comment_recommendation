def problem275_b():
    a,b,c,d,e,f = map(int,input().split())
    #print(a,b,c,d,e,f)
    if a*b*c >= d*e*f:
        print((a*b*c - d*e*f)%998244353)
    else:
        print((d*e*f - a*b*c)%998244353)

if __name__ == '__main__':
    problem275_b()