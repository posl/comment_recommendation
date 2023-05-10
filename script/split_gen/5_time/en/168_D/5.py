def main():
    n,m = map(int,input().split())
    a,b = [0] * m, [0] * m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    print("Yes")
    for i in range(1,n):
        print(a[b.index(i)] if i in b else b[a.index(i)])
