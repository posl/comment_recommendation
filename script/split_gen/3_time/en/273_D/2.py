def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r_i, c_i = map(int, input().split())
        walls.add((r_i, c_i))
    Q = int(input())
    for _ in range(Q):
        d_i, l_i = input().split()
        l_i = int(l_i)
        if d_i == 'L':
            c_s = max(1, c_s - l_i)
            while (r_s, c_s) in walls:
                c_s += 1
        elif d_i == 'R':
            c_s = min(W, c_s + l_i)
            while (r_s, c_s) in walls:
                c_s -= 1
        elif d_i == 'U':
            r_s = max(1, r_s - l_i)
            while (r_s, c_s) in walls:
                r_s += 1
        elif d_i == 'D':
            r_s = min(H, r_s + l_i)
            while (r_s, c_s) in walls:
                r_s -= 1
        print(r_s, c_s)
