def main():
    n,k = map(int,input().split())
    print((n*(n+1)*100*k//2)+(k*(k+1)*n//2))
