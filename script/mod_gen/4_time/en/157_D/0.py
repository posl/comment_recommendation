def readinput():
    n,m,k=list(map(int,input().split()))
    ab=[]
    for _ in range(m):
        a,b=list(map(int,input().split()))
        ab.append((a,b))
    cd=[]
    for _ in range(k):
        c,d=list(map(int,input().split()))
        cd.append((c,d))
    return n,m,k,ab,cd

if __name__ == '__main__':
    readinput()