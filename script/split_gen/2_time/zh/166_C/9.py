def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = [0]*n
    b = [0]*n
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(m):
        if h[a[i]-1] > h[b[i]-1]:
            b[i] = 0
        elif h[a[i]-1] < h[b[i]-1]:
            a[i] = 0
        else:
            a[i] = 0
            b[i] = 0
    a = list(set(a))
    b = list(set(b))
    print(len(a)+len(b))
