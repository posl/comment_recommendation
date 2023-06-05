def readinput():
    n=int(input())
    ab=[]
    for _ in range(n-1):
        a,b=list(map(int,input().split()))
        ab.append((a,b))
    return n,ab

if __name__ == '__main__':
    readinput()