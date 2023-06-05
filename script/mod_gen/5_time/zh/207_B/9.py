def solve():
    a,b,c,d = map(int,input().split())
    if a < b:
        print(-1)
        return
    if c >= d*b:
        print(-1)
        return
    ans = 0
    while a*d > c:
        a += b
        ans += 1
    print(ans)

if __name__ == '__main__':
    solve()