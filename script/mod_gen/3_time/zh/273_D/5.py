def main():
    h, w, r, c = map(int, input().split())
    n = int(input())
    grid = [[0 for i in range(w)] for i in range(h)]
    for i in range(n):
        r_i, c_i = map(int, input().split())
        grid[r_i - 1][c_i - 1] = 1
    q = int(input())
    for i in range(q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for j in range(l):
                if c - 2 >= 0 and grid[r - 1][c - 2] == 0:
                    c -= 1
        elif d == 'R':
            for j in range(l):
                if c < w and grid[r - 1][c] == 0:
                    c += 1
        elif d == 'U':
            for j in range(l):
                if r - 2 >= 0 and grid[r - 2][c - 1] == 0:
                    r -= 1
        else:
            for j in range(l):
                if r < h and grid[r][c - 1] == 0:
                    r += 1
        print(r, c)

if __name__ == '__main__':
    main()