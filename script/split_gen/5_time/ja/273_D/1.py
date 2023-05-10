def main():
    H, W, r, c = map(int, input().split())
    N = int(input())
    wall = set()
    for i in range(N):
        r_i, c_i = map(int, input().split())
        wall.add((r_i, c_i))
    Q = int(input())
    d_l = [list(input().split()) for _ in range(Q)]
    d_l = [[d_l[i][0], int(d_l[i][1])] for i in range(Q)]
    r_c = [r, c]
    d = {'L': [-1, 0], 'R': [1, 0], 'U': [0, -1], 'D': [0, 1]}
    for i in range(Q):
        for _ in range(d_l[i][1]):
            r_c[0] += d[d_l[i][0]][0]
            r_c[1] += d[d_l[i][0]][1]
            if (r_c[0], r_c[1]) in wall:
                r_c[0] -= d[d_l[i][0]][0]
                r_c[1] -= d[d_l[i][0]][1]
                break
    print(r_c[0], r_c[1])
