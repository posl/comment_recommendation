def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a = sorted(a)
    if a[n-1]-a[0] <= k:
        print("Yes")
    else:
        print("No")
