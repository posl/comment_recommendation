def main():
    X, Y, R = map(float, input().split())
    X = int(X*10)
    Y = int(Y*10)
    R = int(R*10)
    ans = 0
    for x in range(X-R, X+R+1):
        d = R**2 - (x-X)**2
        if d < 0:
            continue
        y1 = Y - int(d**0.5)
        y2 = Y + int(d**0.5)
        ans += y2-y1+1
    print(ans)
main()
