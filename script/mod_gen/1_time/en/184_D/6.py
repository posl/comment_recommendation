def solve():
    a,b,c = map(int,input().split())
    ans = 0
    while a+b+c >= 3:
        ans += 1
        if a == 0:
            b -= 1
            c -= 1
            a += 1
        elif b == 0:
            a -= 1
            c -= 1
            b += 1
        elif c == 0:
            a -= 1
            b -= 1
            c += 1
        else:
            a -= 1
            b -= 1
            c -= 1
            a += 1
    print(ans)

if __name__ == '__main__':
    solve()