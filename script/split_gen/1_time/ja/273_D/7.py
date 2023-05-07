def main():
    H, W, r, c = map(int, input().split())
    N = int(input())
    block = set()
    for i in range(N):
        r_i, c_i = map(int, input().split())
        block.add((r_i, c_i))
    Q = int(input())
    for i in range(Q):
        d, l = input().split()
        l = int(l)
        for j in range(l):
            if d == 'L':
                c -= 1
            elif d == 'R':
                c += 1
            elif d == 'U':
                r -= 1
            elif d == 'D':
                r += 1
            if (r, c) in block:
                if d == 'L':
                    c += 1
                elif d == 'R':
                    c -= 1
                elif d == 'U':
                    r += 1
                elif d == 'D':
                    r -= 1
                break
        print(r, c)
