def main():
    n,t=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    t%=s
    for i in range(n):
        if a[i]>t:
            print(i+1,t)
            return
        t-=a[i]
    return
