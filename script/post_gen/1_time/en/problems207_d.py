Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        a, b = map(int, input().split())
        S.append((a, b))
    for _ in range(N):
        c, d = map(int, input().split())
        T.append((c, d))

    for p in range(360):
        for q in range(-10, 11):
            for r in range(-10, 11):
                S_ = [(a * math.cos(math.radians(p)) - b * math.sin(math.radians(p)) + q, a * math.sin(math.radians(p)) + b * math.cos(math.radians(p)) + r) for a, b in S]
                if S_ == T:
                    print('Yes')
                    return
    print('No')

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        a, b = map(int, input().split())
        S.append((a, b))
    for i in range(N):
        c, d = map(int, input().split())
        T.append((c, d))
    # Sを回転させてTに一致するか
    for i in range(4):
        if S == T:
            print('Yes')
            exit()
        S = [(b, -a) for a, b in S]
    # Sを平行移動させてTに一致するか
    for i in range(N):
        dx = T[i][0] - S[0][0]
        dy = T[i][1] - S[0][1]
        S2 = [(a + dx, b + dy) for a, b in S]
        if S2 == T:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 3

def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    t = [list(map(int, input().split())) for _ in range(n)]
    s.sort()
    t.sort()
    for i in range(4):
        if i == 1:
            s = [[-y, x] for x, y in s]
        elif i == 2:
            s = [[-x, -y] for x, y in s]
        elif i == 3:
            s = [[y, -x] for x, y in s]
        for j in range(n):
            dx = t[0][0] - s[j][0]
            dy = t[0][1] - s[j][1]
            for k in range(n):
                s[k][0] += dx
                s[k][1] += dy
            s.sort()
            if s == t:
                print('Yes')
                return
            for k in range(n):
                s[k][0] -= dx
                s[k][1] -= dy
    print('No')

main()

=======
Suggestion 4

def main():
    n = int(input())
    s, t = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        s.append((x, y))
    for _ in range(n):
        x, y = map(int, input().split())
        t.append((x, y))
    if n == 1:
        print('Yes')
        return
    if n == 2:
        if (s[0][0] - s[1][0]) * (t[0][1] - t[1][1]) == (s[0][1] - s[1][1]) * (t[0][0] - t[1][0]):
            print('Yes')
        else:
            print('No')
        return
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if k == i or k == j:
                    continue
                for l in range(n):
                    if l == i or l == j or l == k:
                        continue
                    p1 = (s[i][0] - s[j][0], s[i][1] - s[j][1])
                    p2 = (t[i][0] - t[j][0], t[i][1] - t[j][1])
                    p3 = (s[k][0] - s[l][0], s[k][1] - s[l][1])
                    p4 = (t[k][0] - t[l][0], t[k][1] - t[l][1])
                    if p1[0] * p2[1] == p1[1] * p2[0] and p3[0] * p4[1] == p3[1] * p4[0]:
                        print('Yes')
                        return
    print('No')

=======
Suggestion 5

def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = "No"
    for i in range(4):
        if i != 0:
            S = [[x[1], -x[0]] for x in S]
        for dx in range(-10, 11):
            for dy in range(-10, 11):
                if [[x[0]+dx, x[1]+dy] for x in S] == T:
                    ans = "Yes"
                    break
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = [tuple(map(int, input().split())) for _ in range(n)]
    t = [tuple(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s[i], t[j] = t[j], s[i]
            if set(s) == set(t):
                print('Yes')
                return
            s[i], t[j] = t[j], s[i]
    print('No')

=======
Suggestion 7

def main():
    N = int(input())
    S = [tuple(map(int, input().split())) for _ in range(N)]
    T = [tuple(map(int, input().split())) for _ in range(N)]

    def rotate(p):
        return [(x * cos(p) - y * sin(p), x * sin(p) + y * cos(p)) for x, y in S]

    def translate(q, r):
        return [(x + q, y + r) for x, y in S]

    def match(S, T):
        return sorted(S) == sorted(T)

    for p in range(1, 360):
        if match(rotate(p), T):
            print("Yes")
            break
    else:
        for q in range(-10, 10):
            for r in range(-10, 10):
                if match(translate(q, r), T):
                    print("Yes")
                    break
            else:
                continue
            break
        else:
            print("No")

=======
Suggestion 8

def main():
    import sys
    N = int(sys.stdin.readline())
    S = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
    T = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
    if N == 1:
        print('Yes')
    elif N == 2:
        if (T[0][0] - S[0][0]) * (T[1][1] - S[1][1]) == (T[1][0] - S[1][0]) * (T[0][1] - S[0][1]):
            print('Yes')
        else:
            print('No')
    else:
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                else:
                    x = T[0][0] - S[i][0]
                    y = T[0][1] - S[i][1]
                    if S[j][0] + x == T[1][0] and S[j][1] + y == T[1][1]:
                        break
            else:
                continue
            break
        else:
            print('No')
            return
        for i in range(N):
            if S[i][0] + x != T[i][0] or S[i][1] + y != T[i][1]:
                print('No')
                return
        print('Yes')

=======
Suggestion 9

def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    T = [list(map(int, input().split())) for _ in range(N)]

    def same(S, T):
        for i in range(N):
            for j in range(N):
                if S[i][0] == T[j][0] and S[i][1] == T[j][1]:
                    break
            else:
                return False
        return True

    def rotate(S, theta):
        return [[S[i][0] * cos(theta) - S[i][1] * sin(theta), S[i][0] * sin(theta) + S[i][1] * cos(theta)] for i in range(N)]

    def translate(S, dx, dy):
        return [[S[i][0] + dx, S[i][1] + dy] for i in range(N)]

    if same(S, T):
        print('Yes')
        return

    for i in range(4):
        S = rotate(S, pi / 2)
        if same(S, T):
            print('Yes')
            return

    for dx in range(-100, 101):
        for dy in range(-100, 101):
            S = translate(S, dx, dy)
            if same(S, T):
                print('Yes')
                return

    print('No')

=======
Suggestion 10

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
