def solve():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    blocks = set()
    for i in range(N):
        r_i, c_i = map(int, input().split())
        blocks.add((r_i, c_i))
    Q = int(input())
    for i in range(Q):
        d_i, l_i = input().split()
        l_i = int(l_i)
        if d_i == "L":
            for j in range(l_i):
                if (r_s, c_s - 1) not in blocks:
                    c_s -= 1
        elif d_i == "R":
            for j in range(l_i):
                if (r_s, c_s + 1) not in blocks:
                    c_s += 1
        elif d_i == "U":
            for j in range(l_i):
                if (r_s - 1, c_s) not in blocks:
                    r_s -= 1
        elif d_i == "D":
            for j in range(l_i):
                if (r_s + 1, c_s) not in blocks:
                    r_s += 1
        print(r_s, c_s)

if __name__ == '__main__':
    solve()