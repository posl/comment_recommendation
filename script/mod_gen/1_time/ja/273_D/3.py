def solve():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    blocks = [tuple(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    directions = [input().split() for _ in range(Q)]
    blocks = set(blocks)
    blocks.add((r_s, c_s))
    for d, l in directions:
        if d == "L":
            for i in range(l):
                if (r_s, c_s - 1) not in blocks:
                    c_s -= 1
        elif d == "R":
            for i in range(l):
                if (r_s, c_s + 1) not in blocks:
                    c_s += 1
        elif d == "U":
            for i in range(l):
                if (r_s - 1, c_s) not in blocks:
                    r_s -= 1
        elif d == "D":
            for i in range(l):
                if (r_s + 1, c_s) not in blocks:
                    r_s += 1
        print(r_s, c_s)
solve()

if __name__ == '__main__':
    solve()