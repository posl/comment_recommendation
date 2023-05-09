def readinput():
    n,m=list(map(int,input().split()))
    ab=[]
    for _ in range(m):
        a,b=list(map(int,input().split()))
        ab.append((a,b))
    return n,m,ab

if __name__ == '__main__':
    readinput()