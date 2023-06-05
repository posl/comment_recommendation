def main():
    n,k = map(int,input().split())
    if k == 1:
        print((n+1)%1000000007)
    elif k == n+1:
        print(1%1000000007)
    else:
        print((n*(n+1)//2 - (k-1)*k//2 + 1)%1000000007)
