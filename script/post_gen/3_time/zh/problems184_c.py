Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    elif abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    elif (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    else:
        for i in range(-3, 4):
            for j in range(-3, 4):
                if abs(i) + abs(j) != 3:
                    continue
                if r1 + i + c1 + j == r2 + c2:
                    print(2)
                    return
        print(3)
        return

=======
Suggestion 3

def solution():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    if abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    if abs(r1 + c1 - r2 - c2) <= 3 or abs(r1 - c1 - r2 + c2) <= 3:
        print(2)
        return
    print(3)
    return

=======
Suggestion 4

def main():
    return

=======
Suggestion 5

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            r3 = r1 + i
            c3 = c1 + j
            if abs(r3 - r2) + abs(c3 - c2) <= 3:
                print(2)
                return
    print(3)
    return

=======
Suggestion 6

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
        return

    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return

    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
        print(1)
        return

    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return

    if abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return

    if abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
        return

    print(3)
    return

=======
Suggestion 7

def solve():
    r1,c1 = map(int,input().split())
    r2,c2 = map(int,input().split())
    if r1==r2 and c1==c2:
        print(0)
        return
    if r1+c1==r2+c2 or r1-c1==r2-c2 or abs(r1-r2)+abs(c1-c2)<=3:
        print(1)
        return
    if (r1+c1)%2==(r2+c2)%2:
        print(2)
        return
    for i in range(-3,4):
        for j in range(-3,4):
            if abs(i)+abs(j)>3:
                continue
            if (r1+i+c1+j)%2==(r2+c2)%2:
                print(2)
                return
    print(3)
    return

=======
Suggestion 8

def main():
    print('')

=======
Suggestion 9

def solution():
    r1,c1 = map(int,input().split())
    r2,c2 = map(int,input().split())
    if r1==r2 and c1==c2:
        print(0)
        return
    if (r1+c1)%2 == (r2+c2)%2:
        if abs(r1-r2) + abs(c1-c2) <= 3:
            print(1)
            return
        else:
            print(2)
            return
    else:
        if abs(r1-r2) + abs(c1-c2) <= 3:
            print(2)
            return
        else:
            print(3)
            return

=======
Suggestion 10

def main():
    # input
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    # calc
    if (r1, c1) == (r2, c2):
        print(0)
        return

    if (r1 + c1) == (r2 + c2) or (r1 - c1) == (r2 - c2) or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return

    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return

    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i) + abs(j) <= 3:
                if (r1 + i + c1 + j) % 2 == (r2 + c2) % 2:
                    print(2)
                    return

    print(3)
    return
