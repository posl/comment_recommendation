def solve():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    block = set()
    for _ in range(N):
        r, c = map(int, input().split())
        block.add((r, c))
    Q = int(input())
    for _ in range(Q):
        d, l = input().split()
        l = int(l)
        for _ in range(l):
            if d == 'L' and (r_s, c_s - 1) not in block:
                c_s -= 1
            elif d == 'R' and (r_s, c_s + 1) not in block:
                c_s += 1
            elif d == 'U' and (r_s - 1, c_s) not in block:
                r_s -= 1
            elif d == 'D' and (r_s + 1, c_s) not in block:
                r_s += 1
        print(r_s, c_s)
solve()

if __name__ == '__main__':
    solve()