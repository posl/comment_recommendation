Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i) + abs(j) > 3:
                continue
            r3 = r1 + i
            c3 = c1 + j
            if r3 + c3 == r2 + c2 or r3 - c3 == r2 - c2:
                print(2)
                return
    print(3)
    return

=======
Suggestion 2

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
        return

    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return

    if (r1 + c1 + r2 + c2) % 2 == 0 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
        return

    print(3)
    return

=======
Suggestion 3

def solve():
    from sys import stdin

    read = stdin.readline
    r1, c1 = map(int, read().split())
    r2, c2 = map(int, read().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
        return
    print(3)

=======
Suggestion 4

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        exit()
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        exit()
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        exit()
    for i in range(-3, 4):
        for j in range(-3, 4):
            x, y = r2 + i, c2 + j
            if x + y == r1 + c1 or x - y == r1 - c1:
                print(2)
                exit()
    print(3)

=======
Suggestion 5

def solve(r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return 0
    elif abs(r1 - r2) + abs(c1 - c2) <= 3:
        return 1
    elif (r1 + c1) % 2 == (r2 + c2) % 2:
        return 2
    elif abs((r1 + c1) - (r2 + c2)) <= 3:
        return 2
    elif abs((r1 - c1) - (r2 - c2)) <= 3:
        return 2
    else:
        return 3

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
print(solve(r1, c1, r2, c2))

=======
Suggestion 6

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        exit()
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        exit()
    if (r1 + c1 + r2 + c2) % 2 == 0 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
        exit()
    print(3)

=======
Suggestion 7

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
        return

    if (r2 - r1) == (c2 - c1) or (r2 - r1) == (c1 - c2) or abs(r2 - r1) + abs(c2 - c1) <= 3:
        print(1)
        return

    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return

    for i in range(-3, 4):
        for j in range(-3, 4):
            r3 = r1 + i
            c3 = c1 + j
            if r3 == r2 and c3 == c2:
                print(2)
                return
            if (r3 + c3) % 2 == (r2 + c2) % 2:
                print(3)
                return

=======
Suggestion 8

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs(r1 + c1 - r2 - c2) <= 3 or abs(r1 - c1 - r2 + c2) <= 3:
        print(2)
        return
    print(3)
main()

=======
Suggestion 9

def func(r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return 0
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        return 1
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        return 1
    if abs((r1 + c1) - (r2 + c2)) <= 3:
        return 2
    if abs((r1 - c1) - (r2 - c2)) <= 3:
        return 2
    if abs(r1 - r2) + abs(c1 - c2) <= 6:
        return 2
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        return 2
    return 3

=======
Suggestion 10

def main():
    # input
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    # compute
    if r1==r2 and c1==c2:
        ans = 0
    elif r1+c1==r2+c2 or r1-c1==r2-c2 or abs(r1-r2)+abs(c1-c2)<=3:
        ans = 1
    elif (r1+c1)%2==(r2+c2)%2 or abs(r1-r2)+abs(c1-c2)<=6 or abs(r1+c1-(r2+c2))<=3 or abs(r1-c1-(r2-c2))<=3:
        ans = 2
    else:
        ans = 3
    # output
    print(ans)
