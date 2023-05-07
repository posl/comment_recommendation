def readinput():
    h,w=list(map(int,input().split()))
    s=[]
    for i in range(h):
        s.append(input())
    t=[]
    for i in range(h):
        t.append(input())
    return h,w,s,t

if __name__ == '__main__':
    readinput()