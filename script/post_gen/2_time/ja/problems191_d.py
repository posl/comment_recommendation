Synthesizing 9/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def main():
    x, y, r = map(float, input().split())
    x = int(x * 10000 + 0.5)
    y = int(y * 10000 + 0.5)
    r = int(r * 10000 + 0.5)

    ans = 0
    for i in range(x-r, x+r+1, 10000):
        ans += int((r**2 - (x-i)**2)**0.5 / 10000) * 2 + 1
    print(ans)

=======
Suggestion 3

def main():
    x, y, r = map(float, input().split())
    ans = 0
    for i in range(int(x-r), int(x+r)+1):
        for j in range(int(y-r), int(y+r)+1):
            if (i-x)**2 + (j-y)**2 <= r**2:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    X, Y, R = map(float, input().split())
    X, Y = int(X), int(Y)
    R = int(R)

    count = 0
    for x in range(X - R, X + R + 1):
        for y in range(Y - R, Y + R + 1):
            if (x - X) ** 2 + (y - Y) ** 2 <= R ** 2:
                count += 1

    print(count)

=======
Suggestion 5

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

=======
Suggestion 6

def main():
    x,y,r = map(float, input().split())
    r = int(r)
    cnt = 0
    for i in range(-r, r+1):
        cnt += int((r**2 - (x-i)**2)**0.5)
    print(cnt*4+1)

=======
Suggestion 7

def is_in_circle(x, y, X, Y, R):
    return ((x-X)**2 + (y-Y)**2) <= R**2

=======
Suggestion 8

def main():
    X, Y, R = map(float, input().split())
    R = int(R)
    print(4 * R**2)

=======
Suggestion 9

def calc(r):
    return int(r) * 4 + 1
