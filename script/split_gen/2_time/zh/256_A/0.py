def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for i in range(q)]
    ans = 0
    for i in range(1,n):
        ans += abs(a[i]-a[i-1])
    for i in range(q):
        if x[i] == a[0]:
            ans += abs(a[1]-a[0])
            ans -= abs(a[1]-a[0])
        elif x[i] == a[n-1]:
            ans += abs(a[n-1]-a[n-2])
            ans -= abs(a[n-1]-a[n-2])
        else:
            ans += abs(a[1]-a[0])
            ans += abs(a[n-1]-a[n-2])
            ans -= abs(a[1]-a[0])
            ans -= abs(a[n-1]-a[n-2])
            ans += abs(x[i]-a[0])
            ans += abs(x[i]-a[n-1])
        print(ans)
        ans = 0
