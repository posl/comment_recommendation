def main():
    n=int(input())
    x=[]
    y=[]
    p=[]
    for i in range(n):
        x1,y1,p1=map(int,input().split())
        x.append(x1)
        y.append(y1)
        p.append(p1)
    ans=0
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if p[i]*ans>=abs(x[i]-x[j])+abs(y[i]-y[j]):
                ans+=1
                break
    print(ans)
main()
