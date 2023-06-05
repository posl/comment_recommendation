def main():
    n,x,y = map(int, input().split())
    ans = 0
    for i in range(1,n):
        ans += max(0, n-i-1) * x
    print(ans)
