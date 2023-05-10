def readinput():
    n,m,q=map(int,input().split())
    abcd=[]
    for _ in range(q):
        abcd.append(list(map(int,input().split())))
    return n,m,q,abcd

if __name__ == '__main__':
    readinput()