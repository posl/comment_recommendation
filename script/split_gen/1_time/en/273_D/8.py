def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    grid = [[1 for j in range(W)] for i in range(H)]
    for i in range(N):
        r, c = map(int, input().split())
        grid[r-1][c-1] = 0
    Q = int(input())
    for i in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for j in range(l):
                if c_s-2-j >= 0 and grid[r_s-1][c_s-2-j] == 1:
                    c_s -= 1
        elif d == 'R':
            for j in range(l):
                if c_s+j < W and grid[r_s-1][c_s+j] == 1:
                    c_s += 1
        elif d == 'U':
            for j in range(l):
                if r_s-2-j >= 0 and grid[r_s-2-j][c_s-1] == 1:
                    r_s -= 1
        elif d == 'D':
            for j in range(l):
                if r_s+j < H and grid[r_s+j][c_s-1] == 1:
                    r_s += 1
        print(r_s, c_s)
    return 0
