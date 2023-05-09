def readinput():
    n=int(input())
    ab=[]
    for _ in range(n):
        ai,bi=list(map(int,input().split()))
        ab.append((ai,bi))
    return n,ab

if __name__ == '__main__':
    readinput()