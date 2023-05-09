def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a = [0] + a
    #print(n,m)
    #print(a)
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i+1]
    #print(s)
    ans = -10 ** 9
    for i in range(n-m+1):
        ans = max(ans,s[i+m] - s[i])
    print(ans)
