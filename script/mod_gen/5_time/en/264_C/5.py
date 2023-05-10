def readinput():
    h1,w1=list(map(int,input().split()))
    a=[]
    for _ in range(h1):
        row=list(map(int,input().split()))
        a.append(row)
    h2,w2=list(map(int,input().split()))
    b=[]
    for _ in range(h2):
        row=list(map(int,input().split()))
        b.append(row)
    return h1,w1,a,h2,w2,b

if __name__ == '__main__':
    readinput()