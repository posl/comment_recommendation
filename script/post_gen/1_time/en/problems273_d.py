Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r, c = map(int, input().split())
        walls.add((r, c))
    Q = int(input())
    for _ in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            while l > 0 and (r_s, c_s - 1) not in walls:
                c_s -= 1
                l -= 1
        elif d == 'R':
            while l > 0 and (r_s, c_s + 1) not in walls:
                c_s += 1
                l -= 1
        elif d == 'U':
            while l > 0 and (r_s - 1, c_s) not in walls:
                r_s -= 1
                l -= 1
        else:
            while l > 0 and (r_s + 1, c_s) not in walls:
                r_s += 1
                l -= 1
        print(r_s, c_s)

=======
Suggestion 2

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

=======
Suggestion 3

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
        if d_i == "L":
            for _ in range(int(l_i)):
                if (r_s, c_s-1) not in walls:
                    c_s -= 1
        elif d_i == "R":
            for _ in range(int(l_i)):
                if (r_s, c_s+1) not in walls:
                    c_s += 1
        elif d_i == "U":
            for _ in range(int(l_i)):
                if (r_s-1, c_s) not in walls:
                    r_s -= 1
        elif d_i == "D":
            for _ in range(int(l_i)):
                if (r_s+1, c_s) not in walls:
                    r_s += 1
        print(r_s, c_s)

=======
Suggestion 4

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r_i, c_i = map(int, input().split())
        walls.add((r_i, c_i))
    Q = int(input())
    instructions = []
    for _ in range(Q):
        d_i, l_i = input().split()
        instructions.append((d_i, int(l_i)))
    for d_i, l_i in instructions:
        if d_i == 'L':
            for _ in range(l_i):
                c_s -= 1
                if (r_s, c_s) in walls:
                    c_s += 1
                    break
        elif d_i == 'R':
            for _ in range(l_i):
                c_s += 1
                if (r_s, c_s) in walls:
                    c_s -= 1
                    break
        elif d_i == 'U':
            for _ in range(l_i):
                r_s -= 1
                if (r_s, c_s) in walls:
                    r_s += 1
                    break
        else:
            for _ in range(l_i):
                r_s += 1
                if (r_s, c_s) in walls:
                    r_s -= 1
                    break
        print(r_s, c_s)

=======
Suggestion 5

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    wall = set()
    for i in range(N):
        r, c = map(int, input().split())
        wall.add((r, c))
    Q = int(input())
    d = []
    l = []
    for i in range(Q):
        d_i, l_i = input().split()
        d.append(d_i)
        l.append(int(l_i))
    for i in range(Q):
        if d[i] == "L":
            while True:
                if (r_s, c_s - 1) in wall:
                    break
                else:
                    c_s -= 1
                    l[i] -= 1
                    if l[i] == 0:
                        break
        if d[i] == "R":
            while True:
                if (r_s, c_s + 1) in wall:
                    break
                else:
                    c_s += 1
                    l[i] -= 1
                    if l[i] == 0:
                        break
        if d[i] == "U":
            while True:
                if (r_s - 1, c_s) in wall:
                    break
                else:
                    r_s -= 1
                    l[i] -= 1
                    if l[i] == 0:
                        break
        if d[i] == "D":
            while True:
                if (r_s + 1, c_s) in wall:
                    break
                else:
                    r_s += 1
                    l[i] -= 1
                    if l[i] == 0:
                        break
        print(r_s, c_s)

=======
Suggestion 6

def solve():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r, c = map(int, input().split())
        walls.add((r, c))
    Q = int(input())
    for _ in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for i in range(l):
                c_s -= 1
                if (r_s, c_s) in walls:
                    c_s += 1
                    break
        elif d == 'R':
            for i in range(l):
                c_s += 1
                if (r_s, c_s) in walls:
                    c_s -= 1
                    break
        elif d == 'U':
            for i in range(l):
                r_s -= 1
                if (r_s, c_s) in walls:
                    r_s += 1
                    break
        elif d == 'D':
            for i in range(l):
                r_s += 1
                if (r_s, c_s) in walls:
                    r_s -= 1
                    break
        print(r_s, c_s)

solve()

=======
Suggestion 7

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    wall = set()
    for i in range(N):
        r, c = map(int, input().split())
        wall.add((r, c))
    Q = int(input())
    for i in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for j in range(l):
                if (r_s, c_s - 1) in wall:
                    break
                c_s -= 1
        elif d == 'R':
            for j in range(l):
                if (r_s, c_s + 1) in wall:
                    break
                c_s += 1
        elif d == 'U':
            for j in range(l):
                if (r_s - 1, c_s) in wall:
                    break
                r_s -= 1
        elif d == 'D':
            for j in range(l):
                if (r_s + 1, c_s) in wall:
                    break
                r_s += 1
        print(r_s, c_s)

=======
Suggestion 8

def main():
    h, w, rs, cs = map(int, input().split())
    n = int(input())
    walls = set()
    for _ in range(n):
        r, c = map(int, input().split())
        walls.add((r, c))
    q = int(input())
    for _ in range(q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for _ in range(l):
                cs -= 1
                if (rs, cs) in walls:
                    cs += 1
                    break
        elif d == 'R':
            for _ in range(l):
                cs += 1
                if (rs, cs) in walls:
                    cs -= 1
                    break
        elif d == 'U':
            for _ in range(l):
                rs -= 1
                if (rs, cs) in walls:
                    rs += 1
                    break
        elif d == 'D':
            for _ in range(l):
                rs += 1
                if (rs, cs) in walls:
                    rs -= 1
                    break
        print(rs, cs)

=======
Suggestion 9

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

=======
Suggestion 10

def get_input():
    H, W, r_s, c_s = [int(x) for x in input().split()]
    N = int(input())
    walls = set()
    for _ in range(N):
        r, c = [int(x) for x in input().split()]
        walls.add((r, c))
    Q = int(input())
    instructions = []
    for _ in range(Q):
        d, l = input().split()
        instructions.append((d, int(l)))
    return H, W, r_s, c_s, walls, Q, instructions
