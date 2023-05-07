def solve():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for i in range(-R, R+1):
        x = X + i
        if x < 0 or x >= 10**5:
            continue
        y = int((R**2 - i**2)**0.5)
        y1 = Y + y
        y2 = Y - y
        if y1 >= 0 and y1 < 10**5:
            ans += 1
        if y2 >= 0 and y2 < 10**5 and y1 != y2:
            ans += 1
    print(ans)
