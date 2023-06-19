def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    if k == 1:
        if a[0] % d == 0:
            print(0)
        else:
            print(-1)
    else:
        ans = 0
        for i in range(n-k+1):
            if sum(a[i:i+k]) % d == 0:
                ans += 1
        if ans == 0:
            print(-1)
        else:
            print(ans)
