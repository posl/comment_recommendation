def readinput():
    n,q=map(int,input().split())
    s=input()
    lr=[]
    for _ in range(q):
        l,r=map(int,input().split())
        lr.append((l,r))
    return n,s,q,lr

if __name__ == '__main__':
    readinput()