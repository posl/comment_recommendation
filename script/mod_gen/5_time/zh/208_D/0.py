def readinput():
    n,m=list(map(int,input().split()))
    abclist=[]
    for _ in range(m):
        a,b,c=list(map(int,input().split()))
        abclist.append([a,b,c])
    return n,m,abclist

if __name__ == '__main__':
    readinput()