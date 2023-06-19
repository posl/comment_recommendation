def readinput():
    n,m=list(map(int,input().split()))
    cakes=[]
    for _ in range(n):
        x,y,z=list(map(int,input().split()))
        cakes.append([x,y,z])
    return n,m,cakes

if __name__ == '__main__':
    readinput()