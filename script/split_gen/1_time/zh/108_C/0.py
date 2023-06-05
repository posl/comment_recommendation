def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i%k==0:
            ans += 1
        elif k%2==0 and i%k==k//2:
            ans += 1
    print(ans**3)
