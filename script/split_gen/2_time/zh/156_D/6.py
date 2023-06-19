def main():
    n,a,b = map(int,input().split())
    if a>b:
        a,b = b,a
    ans = n*(n-1)
    ans = ans % (10**9+7)
    ans = ans - (n-a)*(n-b)
    ans = ans % (10**9+7)
    print(ans)
