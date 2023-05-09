def main():
    n,p,q,r,s = map(int,input().split())
    a = list(map(int,input().split()))
    b = a[p-1:q] + a[r-1:s]
    c = a[:p-1] + a[q:r-1] + a[s:]
    c = c[::-1]
    c = c[:p-1] + b + c[p-1:]
    for i in c:
        print(i,end=" ")
