def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    total = sum(a)
    a.sort(reverse=True)
    if a[m-1]*4*m >= total:
        print("Yes")
    else:
        print("No")
