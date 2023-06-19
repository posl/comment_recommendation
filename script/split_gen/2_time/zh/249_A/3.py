def main():
    a,b,c,d,e,f,x=map(int,input().split())
    t=0
    while x>0:
        if a>b:
            t+=b
            x-=1
        else:
            t+=a
            x-=1
        if x==0:
            print("高桥")
            break
        if c>d:
            x-=1
        if x==0:
            print("青木")
            break
