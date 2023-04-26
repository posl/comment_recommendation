Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
    elif (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs(r1 - r2 + c1 - c2) <= 3 or abs(r1 - r2 - c1 + c2) <= 3:
        print(2)
    else:
        print(3)

=======
Suggestion 2

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
        return

    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
        print(1)
        return

    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return

    if abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
        return

    if abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return

    print(3)

main()

=======
Suggestion 3

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
    elif (r1 + c1 + r2 + c2) % 2 == 0 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs(r1 - r2 + c1 - c2) <= 3 or abs(r1 - r2 - c1 + c2) <= 3:
        print(2)
    else:
        print(3)

main()

=======
Suggestion 4

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1 + r2 + c2) % 2 == 0 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs(r1 - r2 + c1 - c2) <= 3 or abs(r1 - r2 - c1 + c2) <= 3:
        print(2)
        return
    print(3)

=======
Suggestion 5

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    ans = 0
    if r1 == r2 and c1 == c2:
        ans = 0
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        ans = 1
    elif (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        ans = 2
    else:
        ans = 3
    print(ans)

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if (r1, c1) == (r2, c2):
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
    if abs(r1 + c1 - r2 - c2) <= 3:
        print(2)
        return
    if abs(r1 - c1 - r2 + c2) <= 3:
        print(2)
        return
    print(3)

=======
Suggestion 7

def main():
    #input
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    #compute
    if r1 == r2 and c1 == c2:
        print(0)
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
    elif (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
    else:
        print(3)

    #output

=======
Suggestion 8

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    print(min(abs(r1-r2)+abs(c1-c2), abs((r1+c1)-(r2+c2)), abs((r1-c1)-(r2-c2))))

=======
Suggestion 9

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    r1 -= r2
    c1 -= c2

    if r1 == c1 == 0:
        print(0)
        return

    if r1 == c1 or r1 == -c1 or abs(r1) + abs(c1) <= 3:
        print(1)
        return

    if (r1 + c1) % 2 == 0 or abs(r1) + abs(c1) <= 6 or abs(r1 - c1) <= 3 or abs(r1 + c1) <= 3:
        print(2)
        return

    print(3)

=======
Suggestion 10

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    # 1. r1, c1 から r2, c2 に移動するまでの最短経路を求める
    # 1.1. r1, c1 から r2, c2 に移動するまでの最短経路を求める
    # 1.1.1. r1, c1 から r2, c2 のどちらかに到達できるまでの最短経路を求める
    #
