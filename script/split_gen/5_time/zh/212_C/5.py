def main():
    n,m = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    ans = 2*10**9
    i = 0
    for x in b:
        while i < n and a[i] <= x:
            i += 1
        if i > 0:
            ans = min(ans,abs(x-a[i-1]))
        if i < n:
            ans = min(ans,abs(x-a[i]))
    print(ans)
