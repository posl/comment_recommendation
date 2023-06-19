def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(m):
        if h[a[i]-1] > h[b[i]-1]:
            h[b[i]-1] = 0
        elif h[a[i]-1] < h[b[i]-1]:
            h[a[i]-1] = 0
        else:
            h[a[i]-1] = 0
            h[b[i]-1] = 0
    count = 0
    for i in range(n):
        if h[i] != 0:
            count += 1
    print(count)
