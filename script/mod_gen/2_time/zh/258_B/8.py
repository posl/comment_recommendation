def readinput():
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    return n,a

if __name__ == '__main__':
    readinput()