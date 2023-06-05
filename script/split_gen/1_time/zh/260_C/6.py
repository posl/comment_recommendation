def main():
    n,x,y = map(int,input().split())
    print(n,x,y)
    ans = 0
    for i in range(1,n):
        ans += max(0, n-i-1) * x
        print(ans)
    for i in range(1,n):
        ans += max(0, n-i-1) * y
        print(ans)
    print(ans)
