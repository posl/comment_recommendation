def main():
    x,y,z,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    sum=[]
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if (i+1)*(j+1)*(k+1)<=k:
                    sum.append(a[i]+b[j]+c[k])
    sum.sort(reverse=True)
    for i in range(k):
        print(sum[i])
