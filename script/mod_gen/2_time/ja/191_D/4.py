def main():
    X, Y, R = map(float, input().split())
    X, Y = int(X), int(Y)
    R = int(R)
    ans = 0
    for x in range(X-R,X+R+1):
        y = int((R**2 - (x-X)**2)**(1/2) + Y)
        ans += y - Y + 1
        y = int(-(R**2 - (x-X)**2)**(1/2) + Y)
        ans += Y - y + 1
    print(ans)

if __name__ == '__main__':
    main()