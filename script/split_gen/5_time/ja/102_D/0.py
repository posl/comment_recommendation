def main():
    n = int(input())
    a = list(map(int,input().split()))
    p = [0]
    for i in range(n):
        p.append(p[i]+a[i])
    ans = 10**9
    for i in range(1,n-2):
        l = p[i]
        r = p[-1]-p[i]
        ans = min(ans,abs(l-r))
    print(ans)
