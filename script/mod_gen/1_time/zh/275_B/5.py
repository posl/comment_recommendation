def problem275_b():
    a,b,c,d,e,f = map(int,input().split())
    if a*b*c >= d*e*f:
        print((a*b*c-d*e*f)%998244353)
    else:
        print(0)

if __name__ == '__main__':
    problem275_b()