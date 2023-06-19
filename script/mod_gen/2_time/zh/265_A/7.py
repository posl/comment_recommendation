def solve():
    x,y,n = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i % 3 == 0:
            ans += x
        else:
            ans += y
    print(ans)

if __name__ == '__main__':
    solve()