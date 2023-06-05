def main():
    n,k = map(int,input().split())
    ans = 0
    if k%2 == 0:
        for i in range(1,n+1):
            if i%k == 0:
                ans += 1
        ans = ans**3
    else:
        for i in range(1,n+1):
            if i%k == 0:
                ans += 1
        for i in range(1,n+1):
            if i%k == k//2:
                ans += 1
        ans = ans**3
    print(ans)
