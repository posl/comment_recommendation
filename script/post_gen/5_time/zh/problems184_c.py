Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve(r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return 0
    if r1 + c1 == r2 + c2:
        return 1
    if r1 - c1 == r2 - c2:
        return 1
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        return 1
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        return 2
    if abs(r1 - r2) + abs(c1 - c2) <= 6:
        return 2
    if abs((r1 + c1) - (r2 + c2)) <= 3:
        return 2
    if abs((r1 - c1) - (r2 - c2)) <= 3:
        return 2
    return 3

=======
Suggestion 3

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
    if abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    if abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
        return
    print(3)
    return

=======
Suggestion 4

def main():
    r1,c1 = map(int, input().split())
    r2,c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2)+abs(c1-c2) <= 3:
        print(1)
        return
    if (r1+c1)%2 == (r2+c2)%2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i)+abs(j) <= 3:
                if r1+c1+i == r2+c2+j or r1-c1+i == r2-c2+j:
                    print(2)
                    return
    print(3)
    return

=======
Suggestion 5

def main():
    r1,c1=map(int,input().split())
    r2,c2=map(int,input().split())
    if r1==r2 and c1==c2:
        print(0)
        return
    if r1+c1==r2+c2 or r1-c1==r2-c2 or abs(r1-r2)+abs(c1-c2)<=3:
        print(1)
        return
    if (r1+c1+r2+c2)%2==0 or abs(r1-r2)+abs(c1-c2)<=6 or abs((r1+c1)-(r2+c2))<=3 or abs((r1-c1)-(r2-c2))<=3:
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
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i) + abs(j) == 3:
                if r1 + i + c1 + j == r2 + c2:
                    print(2)
                    return
    print(3)

main()

=======
Suggestion 7

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
    for dr in range(-3, 4):
        for dc in range(-3, 4):
            if (r1 + dr + c1 + dc) % 2 == (r2 + c2) % 2:
                print(2)
                return
    print(3)

=======
Suggestion 8

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
    if abs(r1 + c1 - r2 - c2) <= 3 or abs(r1 - c1 - r2 + c2) <= 3:
        print(2)
        return
    print(3)
