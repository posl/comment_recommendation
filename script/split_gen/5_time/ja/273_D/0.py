def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    wall = [[0 for col in range(W)] for row in range(H)]
    for i in range(N):
        r, c = map(int, input().split())
        wall[r-1][c-1] = 1
    Q = int(input())
    for i in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for j in range(l):
                if cs - 1 >= 0 and wall[rs-1][cs-1] == 0:
                    cs -= 1
        elif d == 'R':
            for j in range(l):
                if cs + 1 < W and wall[rs-1][cs] == 0:
                    cs += 1
        elif d == 'U':
            for j in range(l):
                if rs - 1 >= 0 and wall[rs-2][cs-1] == 0:
                    rs -= 1
        elif d == 'D':
            for j in range(l):
                if rs + 1 < H and wall[rs][cs-1] == 0:
                    rs += 1
        print(rs, cs)
