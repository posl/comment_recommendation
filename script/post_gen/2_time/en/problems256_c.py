Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print(solve(h1, h2, h3, w1, w2, w3))

=======
Suggestion 2

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for a in range(1, h1 + 1):
        for b in range(1, h2 + 1):
            for c in range(1, h3 + 1):
                for d in range(1, w1 + 1):
                    for e in range(1, w2 + 1):
                        for f in range(1, w3 + 1):
                            if a + b + c == h1 and a + d + e == w1 and b + d + f == w2 and c + e + f == w3:
                                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    ans = 0
    for a in range(1, 31):
        for b in range(1, 31):
            for c in range(1, 31):
                for d in range(1, 31):
                    for e in range(1, 31):
                        for f in range(1, 31):
                            for g in range(1, 31):
                                for i in range(1, 31):
                                    for j in range(1, 31):
                                        if h[0] == a + b + c and h[1] == d + e + f and h[2] == g + i + j and w[0] == a + d + g and w[1] == b + e + i and w[2] == c + f + j:
                                            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    ans = 0
    for a in range(1,31):
        for b in range(1,31):
            for c in range(1,31):
                for d in range(1,31):
                    for e in range(1,31):
                        for f in range(1,31):
                            if a+b+c == h1 and d+e+f == h2 and a+d == w1 and b+e == w2 and c+f == w3 and c+e == h3:
                                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for x1 in range(1, h1):
        for x2 in range(1, h2):
            for x3 in range(1, h3):
                for y1 in range(1, w1):
                    for y2 in range(1, w2):
                        for y3 in range(1, w3):
                            if (x1+x2+x3 == h1 and x1+x2+x3 == h2 and x1+x2+x3 == h3 and
                                y1+y2+y3 == w1 and y1+y2+y3 == w2 and y1+y2+y3 == w3 and
                                x1+y1 == x2+y2 == x3+y3):
                                ans += 1
    print(ans)

=======
Suggestion 6

def check(h, w):
    if h[0] == w[0] + w[1] + w[2] and h[1] == w[0] + w[1] + w[2] and h[2] == w[0] + w[1] + w[2]:
        if w[0] == h[0] + h[1] + h[2] and w[1] == h[0] + h[1] + h[2] and w[2] == h[0] + h[1] + h[2]:
            return True
    return False

=======
Suggestion 7

def solve(h1, h2, h3, w1, w2, w3):
    s = set()
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                if i + j + k == h1 and i + k + j == h2 and j + k + i == h3 and i + j + k == w1 and i + k + j == w2 and j + k + i == w3:
                    s.add((i, j, k))
    return len(s)

=======
Suggestion 8

def check(h1,h2,h3,w1,w2,w3):
    if h1 == h2 == h3 and w1 == w2 == w3:
        return True
    else:
        return False

=======
Suggestion 9

def main():
    h = [int(x) for x in input().split()]
    w = [int(x) for x in input().split()]
    print(h)
    print(w)

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
