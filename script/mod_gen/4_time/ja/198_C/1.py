def solve():
    R, X, Y = map(int, input().split())
    if R**2 == X**2 + Y**2:
        print(1)
    elif R**2 > X**2 + Y**2:
        print(2)
    else:
        ans = 0
        while R**2 < X**2 + Y**2:
            ans += 1
            X = X // 2
            Y = Y // 2
        print(ans)

if __name__ == '__main__':
    solve()