def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    print(a)
    print(n,k)
    print(a[0:k])
    print(a[n-k:n])
    print(max(a[0:k])+max(a[n-k:n]))
