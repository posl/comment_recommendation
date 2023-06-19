def main():
    n,m,q = map(int,input().split())
    a = [0 for i in range(q)]
    b = [0 for i in range(q)]
    c = [0 for i in range(q)]
    d = [0 for i in range(q)]
    for i in range(q):
        a[i],b[i],c[i],d[i] = map(int,input().split())
    print(a)
    print(b)
    print(c)
    print(d)
