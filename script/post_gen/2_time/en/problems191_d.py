Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10 ** 4)
    Y = int(Y * 10 ** 4)
    R = int(R * 10 ** 4)
    ans = 0
    for x in range(X - R, X + R + 1):
        if x % 10 ** 4 == 0:
            y = int((R ** 2 - (x - X) ** 2) ** 0.5 + Y)
            ans += y // 10 ** 4 - (Y - R) // 10 ** 4 + 1
    print(ans)

=======
Suggestion 2

def main():
    x, y, r = map(float, input().split())
    x = int(x * 10000)
    y = int(y * 10000)
    r = int(r * 10000)
    ans = 0
    for i in range(int(x - r), int(x + r) + 1):
        if i < 0:
            continue
        if i > 10 ** 5:
            break
        a = (r ** 2 - (i - x) ** 2) ** 0.5
        ans += int(y + a) - int(y - a) + 1
    print(ans)

=======
Suggestion 3

def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for x in range(X - R, X + R + 1):
        if x < 0 or x > 10 ** 10:
            continue
        y = int((R ** 2 - (x - X) ** 2) ** 0.5)
        ans += (Y + y) // 10000 - (Y - y) // 10000 + 1
    print(ans)

=======
Suggestion 4

def circle(x, y, r):
    count = 0
    for i in range(int(x-r), int(x+r)+1):
        for j in range(int(y-r), int(y+r)+1):
            if (i-x)**2 + (j-y)**2 <= r**2:
                count += 1
    return count

x, y, r = map(float, input().split())
print(circle(x, y, r))

=======
Suggestion 5

def main():
    x, y, r = map(float, input().split())
    x, y = int(x*10000), int(y*10000)
    r = int(r*10000)
    ans = 0
    for i in range(x-r, x+r+1):
        if i < 0 or i > 10**5:
            continue
        h = (r**2 - (x-i)**2)**0.5
        ans += int(y+h)//10000 - max(0, (y-h)//10000) + 1
    print(ans)

=======
Suggestion 6

def main():
    X, Y, R = map(float, input().split())
    #print(X, Y, R)
    ans = 0
    for x in range(int(X - R), int(X + R) + 1):
        for y in range(int(Y - R), int(Y + R) + 1):
            if (x - X) ** 2 + (y - Y) ** 2 <= R ** 2:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    # Write your code here
    x, y, r = map(float, input().split())
    x = int(x)
    y = int(y)
    r = int(r)
    count = 0
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                count += 1
    print(count)

=======
Suggestion 8

def main():
    X, Y, R = map(float, input().split())
    print(int(R**2 - X**2 - Y**2 + 1))

=======
Suggestion 9

def dist(x,y):
    return (x**2+y**2)**0.5

=======
Suggestion 10

def f(x, y, r):
    return 4 * (int(r) - y) * (int(r) + y) + 1
