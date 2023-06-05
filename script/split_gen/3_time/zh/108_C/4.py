def main():
    n,k = map(int,input().split())
    ans = 0
    for a in range(1,n+1):
        ans += (n//a)*max(0,a-k)
        ans += max(0,(n%a)-k+1)
        if k == 0:
            ans -= 1
    print(ans)
