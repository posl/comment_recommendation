Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2:
        print(1)
        return
    if r1 - c1 == r2 - c2:
        print(1)
        return
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1 + r2 + c2) % 2 == 0:
        print(2)
        return
    if abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    if abs((r1 + c1) - (r2 + c2)) <= 3:
        print(2)
        return
    if abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
        return
    print(3)

=======
Suggestion 2

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
    elif (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
    else:
        print(3)

=======
Suggestion 3

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
        exit()

    if r1 + c1 == r2 + c2:
        print(1)
        exit()

    if r1 - c1 == r2 - c2:
        print(1)
        exit()

    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        exit()

    if (r1 + c1)%2 == (r2 + c2)%2:
        print(2)
        exit()

    if abs(r1 + c1 - r2 - c2) <= 3:
        print(2)
        exit()

    if abs(r1 - c1 - r2 + c2) <= 3:
        print(2)
        exit()

    if abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        exit()

    print(3)
    exit()

=======
Suggestion 4

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if (r1, c1) == (r2, c2):
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1 + r2 + c2) % 2 == 0 or abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    print(3)

=======
Suggestion 5

def ryuma(r1,c1,r2,c2):
    if r1==r2 and c1==c2:
        return 0
    elif r1+c1==r2+c2 or r1-c1==r2-c2 or abs(r1-r2)+abs(c1-c2)<=3:
        return 1
    elif (r1+c1)%2==(r2+c2)%2:
        return 2
    else:
        return 3
