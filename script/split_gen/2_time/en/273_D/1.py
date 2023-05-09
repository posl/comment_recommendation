def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r_i, c_i = map(int, input().split())
        walls.add((r_i, c_i))
    Q = int(input())
    d = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    for _ in range(Q):
        d_i, l_i = input().split()
        l_i = int(l_i)
        for _ in range(l_i):
            r_s += d[d_i][0]
            c_s += d[d_i][1]
            if (r_s, c_s) in walls:
                r_s -= d[d_i][0]
                c_s -= d[d_i][1]
        print(r_s, c_s)
