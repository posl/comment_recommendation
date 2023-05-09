def problem265_a():
    x, y, n = map(int, input().split())
    ans = 0
    if n % 3 == 0:
        ans = (n//3) * y
    elif n % 3 == 1:
        ans = (n//3) * y + x
    else:
        ans = (n//3) * y + x * 2
    print(ans)
