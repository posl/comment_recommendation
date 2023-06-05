def readinput():
    n,c=list(map(int,input().split()))
    abclist=[]
    for _ in range(n):
        abc=list(map(int,input().split()))
        abclist.append(abc)
    return n,c,abclist

if __name__ == '__main__':
    readinput()