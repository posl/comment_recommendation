def solve():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    t = [list(map(int, input().split())) for _ in range(n)]
    def rotate(s, p):
        from math import cos, sin, radians
        return [[cos(radians(p)) * x[0] - sin(radians(p)) * x[1], sin(radians(p)) * x[0] + cos(radians(p)) * x[1]] for x in s]
    def move(s, q, r):
        return [[x[0] + q, x[1] + r] for x in s]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                p = t[i][0] - s[j][0]
                q = t[i][1] - s[j][1]
                s2 = move(rotate(s, p), q, 0)
                if all([x in s2 for x in t]):
                    print('Yes')
                    return
    print('No')
