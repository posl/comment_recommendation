def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(m):
        a[n-1] = a[n-1]//2
        a.sort()
    print(sum(a))
