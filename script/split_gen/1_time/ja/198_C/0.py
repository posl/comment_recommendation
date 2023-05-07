def solve():
    R, X, Y = map(int, input().split())
    if R * R == X * X + Y * Y:
        print(1)
    elif R * R > X * X + Y * Y:
        print(2)
    else:
        ans = 0
        while True:
            ans += 1
            if (R * ans) * (R * ans) >= X * X + Y * Y:
                break
        print(ans)
