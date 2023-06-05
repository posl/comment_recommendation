def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(m):
        if h[a[i]-1] <= h[b[i]-1]:
            h[a[i]-1] = 0
        if h[b[i]-1] <= h[a[i]-1]:
            h[b[i]-1] = 0
    print(h.count(0))
