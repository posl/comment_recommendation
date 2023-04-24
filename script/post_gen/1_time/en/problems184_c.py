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
    elif (r1 + c1 + r2 + c2) % 2 == 0 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
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
    elif abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    elif (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    elif abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    elif abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    elif abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    elif abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    elif abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    elif abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    elif abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    elif abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    elif abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    elif abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    elif abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        return
    else:
        print(3)
        return

=======
Suggestion 3

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    d = abs(r1 - r2) + abs(c1 - c2)
    if d == 0:
        print(0)
    elif d <= 3:
        print(1)
    elif (d % 2 == 0) or (d <= 6):
        print(2)
    else:
        print(3)

=======
Suggestion 4

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(0)
        return
    if abs(x1 - x2) + abs(y1 - y2) <= 3:
        print(1)
        return
    if abs(x1 - x2) + abs(y1 - y2) <= 6:
        print(2)
        return
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        print(2)
        return
    if abs(x1 - x2) + abs(y1 - y2) <= 6 or abs((x1 + y1) - (x2 + y2)) <= 3 or abs((x1 - y1) - (x2 - y2)) <= 3:
        print(2)
        return
    print(3)
    return

=======
Suggestion 5

def main():
    r1,c1 = map(int, input().split())
    r2,c2 = map(int, input().split())
    if r1==r2 and c1==c2:
        print(0)
        return
    if abs(r1-r2)+abs(c1-c2) <= 3:
        print(1)
        return
    if (r1+c1) == (r2+c2) or (r1-c1) == (r2-c2) or abs(r1-r2)+abs(c1-c2) <= 6:
        print(2)
        return
    if abs((r1+c1)-(r2+c2)) <= 3 or abs((r1-c1)-(r2-c2)) <= 3:
        print(2)
        return
    if abs(r1-r2)+abs(c1-c2) <= 6:
        print(2)
        return
    print(3)
    return

=======
Suggestion 6

def ryuma(r1,c1,r2,c2):
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
    if abs((r1 + c1) - (r2 + c2)) <= 3:
        return 2
    if abs((r1 - c1) - (r2 - c2)) <= 3:
        return 2
    return 3

r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())
print(ryuma(r1,c1,r2,c2))

=======
Suggestion 7

def main():
    from sys import stdin
    from collections import deque
    r1, c1 = map(int, stdin.readline().split())
    r2, c2 = map(int, stdin.readline().split())
    q = deque()
    q.append((r1, c1, 0))
    visited = set()
    visited.add((r1, c1))
    while q:
        r, c, d = q.popleft()
        if r == r2 and c == c2:
            print(d)
            return
        for dr in range(-3, 4):
            for dc in range(-3, 4):
                if abs(dr) + abs(dc) <= 3:
                    nr = r + dr
                    nc = c + dc
                    if (nr, nc) not in visited:
                        q.append((nr, nc, d + 1))
                        visited.add((nr, nc))

=======
Suggestion 8

def main():
    r1,c1=map(int,input().split())
    r2,c2=map(int,input().split())
    print(min(abs(r1-r2)+abs(c1-c2),abs((r1-c1)-(r2-c2)),abs((r1+c1)-(r2+c2))//2))

=======
Suggestion 9

def get_dist(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

=======
Suggestion 10

def get_pos(x, y):
    return (x, y)
