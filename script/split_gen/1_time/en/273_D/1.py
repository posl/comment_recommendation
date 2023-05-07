def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r_i, c_i = map(int, input().split())
        walls.add((r_i, c_i))
    Q = int(input())
    r_t = r_s
    c_t = c_s
    for _ in range(Q):
        d_i, l_i = input().split()
        l_i = int(l_i)
        if d_i == 'L':
            while l_i > 0:
                if (r_t, c_t - 1) not in walls:
                    c_t -= 1
                l_i -= 1
        elif d_i == 'R':
            while l_i > 0:
                if (r_t, c_t + 1) not in walls:
                    c_t += 1
                l_i -= 1
        elif d_i == 'U':
            while l_i > 0:
                if (r_t - 1, c_t) not in walls:
                    r_t -= 1
                l_i -= 1
        else:
            while l_i > 0:
                if (r_t + 1, c_t) not in walls:
                    r_t += 1
                l_i -= 1
        print(r_t, c_t)
