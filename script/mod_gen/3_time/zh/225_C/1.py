def readinput():
    n,m=list(map(int,input().split()))
    b=[]
    for _ in range(n):
        b.append(list(map(int,input().split())))
    return n,m,b

if __name__ == '__main__':
    readinput()