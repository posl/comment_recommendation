def main():
    n,m = map(int,input().split())
    a=[0]*n
    for i in range(m):
        aa,bb=map(int,input().split())
        if aa==1:
            a[bb-1]=1
        if bb==n:
            a[aa-1]=1
    aa=0
    for i in range(n):
        if a[i]==1:
            aa+=1
    if aa>0:
        print(aa)
    else:
        print(0)
