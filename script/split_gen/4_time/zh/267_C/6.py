def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(1,m+1):
        ans += i*a[i-1]
    tmp = ans
    for i in range(m,n):
        tmp += (i+1)*a[i]
        tmp -= (i-m+1)*a[i-m]
        ans = max(ans,tmp)
    print(ans)
