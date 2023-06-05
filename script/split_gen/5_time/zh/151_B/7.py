def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n * m - sum(a) > k:
        print(-1)
    else:
        print(max(0,n*m-sum(a)))
