def main():
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    l=list(map(int,input().split()))
    p=[0 for i in range(n)]
    for i in range(k):
        p[a[i]-1]=i+1
    for i in range(q):
        if p[l[i]-1]!=0:
            if l[i]!=1:
                if p[l[i]-2]==0:
                    p[l[i]-2]=p[l[i]-1]
                    p[l[i]-1]=0
            if l[i]!=n:
                if p[l[i]]==0:
                    p[l[i]]=p[l[i]-1]
                    p[l[i]-1]=0
    for i in range(n):
        print(p[i],end=' ')
