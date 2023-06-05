def readinput():
    n,w=map(int,input().split())
    ab=[]
    for _ in range(n):
        a,b=map(int,input().split())
        ab.append((a,b))
    return n,w,ab

if __name__ == '__main__':
    readinput()