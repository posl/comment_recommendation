def readinput():
    n,k = map(int, input().split())
    p=[]
    for i in range(n):
        p.append(list(map(int, input().split())))
    return n,k,p

if __name__ == '__main__':
    readinput()