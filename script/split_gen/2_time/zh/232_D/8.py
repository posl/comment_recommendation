def main():
    n,m=map(int,input().split())
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(m):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(m):
        x,y=map(int,input().split())
        c.append(x)
        d.append(y)
    for i in range(m):
        if a[i] in c and b[i] in d:
            continue
        elif a[i] in d and b[i] in c:
            continue
        else:
            print("No")
            break
    else:
        print("Yes")
