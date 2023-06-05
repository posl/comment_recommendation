def main():
    n,m=map(int,input().split())
    a,b=[],[]
    for i in range(m):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(1,n+1):
        print(a.count(i)+b.count(i))
