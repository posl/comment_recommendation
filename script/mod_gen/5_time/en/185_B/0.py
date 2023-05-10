def readinput():
    n,m,t=map(int,input().split())
    ab=[]
    for _ in range(m):
        a,b=map(int,input().split())
        ab.append((a,b))
    return n,m,t,ab

if __name__ == '__main__':
    readinput()