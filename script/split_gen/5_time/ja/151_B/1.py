def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    sum = sum(a)
    if n*m - sum <= k:
        print(max(0,n*m - sum))
    else:
        print(-1)
