def main():
    n,m = map(int,input().split())
    a=[]
    b=[]
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    print(a,b)
