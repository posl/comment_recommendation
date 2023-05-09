def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for i in range(N):
        r_i, c_i = map(int, input().split())
        walls.add((r_i, c_i))
    Q = int(input())
    d = {'L':(-1, 0), 'R':(1, 0), 'U':(0, -1), 'D':(0, 1)}
    for i in range(Q):
        d_i, l_i = input().split()
        l_i = int(l_i)
        for j in range(l_i):
            r_s += d[d_i][0]
            c_s += d[d_i][1]
            if (r_s, c_s) in walls:
                r_s -= d[d_i][0]
                c_s -= d[d_i][1]
        print(r_s, c_s)
    return
