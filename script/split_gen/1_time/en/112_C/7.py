def check(x,y,h):
    for i in range(n):
        if h!=max(H-abs(X[i]-x)-abs(Y[i]-y),0):
            return False
    return True
n=int(input())
X=[]
Y=[]
H=[]
for i in range(n):
    x,y,h=map(int,input().split())
    X.append(x)
    Y.append(y)
    H.append(h)
for i in range(n):
    if H[i]>0:
        x=X[i]
        y=Y[i]
        h=H[i]
        break
for i in range(101):
    for j in range(101):
        if check(i,j,h):
            print(i,j,h)
            exit()
