def main():
    n,m=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(m)]
    b=[list(map(int,input().split())) for _ in range(m)]
    a.sort()
    b.sort()
    for i in range(m):
        a[i][0]-=1
        a[i][1]-=1
        b[i][0]-=1
        b[i][1]-=1
    for i in range(m):
        a[i][0],a[i][1]=a[i][1],a[i][0]
        b[i][0],b[i][1]=b[i][1],b[i][0]
    a.sort()
    b.sort()
    for i in range(m):
        a[i][0],a[i][1]=a[i][1],a[i][0]
        b[i][0],b[i][1]=b[i][1],b[i][0]
    for i in range(m):
        if a[i]!=b[i]:
            print("No")
            return
    print("Yes")
    return
