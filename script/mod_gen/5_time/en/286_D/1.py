def readinput():
    n,x=list(map(int,input().split()))
    ab=[]
    for _ in range(n):
        ab.append(list(map(int,input().split())))
    return n,x,ab

if __name__ == '__main__':
    readinput()