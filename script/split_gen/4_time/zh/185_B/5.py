def main():
    n,m,t=map(int,input().split())
    a=[]
    b=[]
    for i in range(m):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    now=0
    cnt=0
    for i in range(m):
        if now>=a[i]:
            now+=b[i]-a[i]
        else:
            cnt+=a[i]-now
            now=b[i]
        if now>=n:
            print('Yes')
            return
    cnt+=t-now
    if cnt>=n:
        print('Yes')
    else:
        print('No')
    return
