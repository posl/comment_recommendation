def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.insert(0,0)
    b = [0]*(n+1)
    b[x] = 1
    for i in range(1,n+1):
        if b[a[i]] == 1:
            b[i] = 1
    print(sum(b))
