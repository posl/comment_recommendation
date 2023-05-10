def readinput():
    n,m=map(int,input().split())
    k=[]
    s=[]
    for _ in range(m):
        k.append(int(input()))
        s.append(list(map(int,input().split())))
    p=list(map(int,input().split()))
    return n,m,k,s,p

if __name__ == '__main__':
    readinput()