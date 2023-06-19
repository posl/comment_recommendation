def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    print(a)
    print(a[n-k])
    print(a[n-1])
    if a[n-k] == a[n-1]:
        print(n)
    else:
        print(n-k)
