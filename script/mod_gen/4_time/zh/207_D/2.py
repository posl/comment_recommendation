def solve():
    # N = 3
    # S = [(0, 0), (0, 1), (1, 0)]
    # T = [(2, 0), (3, 0), (3, 1)]
    # N = 3
    # S = [(1, 0), (1, 1), (3, 0)]
    # T = [(-1, 0), (-1, 1), (-3, 0)]
    # N = 4
    # S = [(0, 0), (2, 9), (10, -2), (-6, -7)]
    # T = [(0, 0), (2, 9), (10, -2), (-6, -7)]
    # N = 6
    # S = [(10, 5), (-9, 3), (1, -5), (-6, -5), (6, 9), (-9, 0)]
    # T = [(-7, -10), (-10, -5), (5, 4), (9, 0), (0, -10), (-10, -2)]
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(tuple(map(int, input().split())))
    for i in range(N):
        T.append(tuple(map(int, input().split())))
    def rotate(s, t):
        p = t[0] - s[0]
        q = t[1] - s[1]
        if p == 0:
            if q == 0:
                return True
            else:
                return False
        else:
            if q == 0:
                return False
            else:
                return True
    def translate(s, t):
        p = t[0] - s[0]
        q = t[1] - s[1]
        if p == 0:
            if q == 0:
                return True
            else:
                return False
        else:
            if q == 0:
                return False
            else:
                return True
    def check(s, t):
        if rotate(s, t):
            return True
        else:
            return False
    for i in range(N):
        flag = False
        for

if __name__ == '__main__':
    solve()