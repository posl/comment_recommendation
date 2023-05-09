def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    total = sum(a)
    if n < total:
        print(-1)
    else:
        print(n-total)
