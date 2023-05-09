def main():
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if a[i] <= x:
            ans += a[i]
        else:
            ans += x
    print(ans)
