def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    block = set()
    for i in range(N):
        r_i, c_i = map(int, input().split())
        block.add((r_i, c_i))
    Q = int(input())
    for i in range(Q):
        d_i, l_i = input().split()
        l_i = int(l_i)
        if d_i == 'L':
            for j in range(l_i):
                if (r_s, c_s - 1) in block:
                    break
                else:
                    c_s -= 1
        if d_i == 'R':
            for j in range(l_i):
                if (r_s, c_s + 1) in block:
                    break
                else:
                    c_s += 1
        if d_i == 'U':
            for j in range(l_i):
                if (r_s - 1, c_s) in block:
                    break
                else:
                    r_s -= 1
        if d_i == 'D':
            for j in range(l_i):
                if (r_s + 1, c_s) in block:
                    break
                else:
                    r_s += 1
        print(r_s, c_s)
