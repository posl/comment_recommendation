def main():
    a,b,c=map(int,input().split())
    if a==0 and b==0:
        print(99)
        exit()
    if a==0 and c==0:
        print(99)
        exit()
    if b==0 and c==0:
        print(99)
        exit()
    if a==0:
        print(99)
        exit()
    if b==0:
        print(99)
        exit()
    if c==0:
        print(99)
        exit()
    s=a+b+c
    t=a/s
    u=b/s
    v=c/s
    ans=1+t*2+u*2+v*2+t*u*2+t*v*2+u*v*2
    print(ans)
main()
