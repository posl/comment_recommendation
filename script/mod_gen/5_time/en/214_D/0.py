def readinput():
    n=int(input())
    edges=[]
    for _ in range(n-1):
        u,v,w=list(map(int,input().split()))
        edges.append((u,v,w))
    return n,edges

if __name__ == '__main__':
    readinput()