def main():
    a,b,n = map(int,input().split())
    if b-1 <= n:
        print((a*(b-1)//b)-a*((b-1)//b))
    else:
        print((a*n//b)-a*(n//b))
