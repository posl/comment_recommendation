def solve():
    a,b,k = map(int, input().split())
    if a >= b:
        print(0)
        return
    ans = 0
    while a < b:
        a += a * k
        ans += 1
    print(ans)

if __name__ == '__main__':
    solve()