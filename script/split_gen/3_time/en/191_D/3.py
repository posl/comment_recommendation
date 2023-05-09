def main():
    X, Y, R = map(float, input().split())
    import math
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for x in range(X - R, X + R + 1):
        if x < 0 or x > 10**5 * 10000:
            continue
        y = int(math.sqrt(R**2 - (x - X)**2)) + Y
        if y < 0 or y > 10**5 * 10000:
            continue
        ans += 1
    for x in range(X - R, X + R + 1):
        if x < 0 or x > 10**5 * 10000:
            continue
        y = -int(math.sqrt(R**2 - (x - X)**2)) + Y
        if y < 0 or y > 10**5 * 10000:
            continue
        ans += 1
    print(ans)
