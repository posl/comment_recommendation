def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    for i in b:
        c.append(a[i-1])
    c.sort()
    for i in range(k):
        a.remove(c[i])
    if a[-1]>c[-1]:
        print("Yes")
    else:
        print("No")
