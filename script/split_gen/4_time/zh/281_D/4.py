def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if k == 1:
        if a[0]%d == 0:
            print(-1)
        else:
            print(a[0])
    else:
        if a[0]%d == 0 and a[1]%d == 0:
            print(-1)
        else:
            print(a[0]+a[1])
