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
        if d == 'L':
            for j in range(l):
                if (r, c - 1) not in block:
                    c -= 1
        elif d == 'R':
            for j in range(l):
                if (r, c + 1) not in block:
                    c += 1
        elif d == 'U':
            for j in range(l):
                if (r - 1, c) not in block:
                    r -= 1
        elif d == 'D':
            for j in range(l):
                if (r + 1, c) not in block:
                    r += 1
        print(r, c)

if __name__ == '__main__':
    main()