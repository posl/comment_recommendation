def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for i in range(X-R, X+R+1):
        d = R * R - (X-i) * (X-i)
        if d >= 0:
            dy = int(d**0.5)
            ans += (Y + dy) // 10000 - (Y - dy) // 10000 + 1
    print(ans)
