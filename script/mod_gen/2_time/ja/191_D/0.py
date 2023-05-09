def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10**4)
    Y = int(Y * 10**4)
    R = int(R * 10**4)
    ans = 0
    for x in range(X - R, X + R + 1):
        y2 = R**2 - (x - X)**2
        if y2 >= 0:
            y = int(y2**0.5)
            ans += 4 * (y // 10**4) + 1
            if y % 10**4 == 0:
                ans -= 1
            if (x - X)**2 + (y - Y)**2 <= R**2:
                ans -= 1
    print(ans)
main()

if __name__ == '__main__':
    main()