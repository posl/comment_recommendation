def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r, c = map(int, input().split())
        walls.add((r, c))
    Q = int(input())
    r = r_s
    c = c_s
    for _ in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for _ in range(l):
                if (r, c - 1) not in walls:
                    c -= 1
        elif d == 'R':
            for _ in range(l):
                if (r, c + 1) not in walls:
                    c += 1
        elif d == 'U':
            for _ in range(l):
                if (r - 1, c) not in walls:
                    r -= 1
        elif d == 'D':
            for _ in range(l):
                if (r + 1, c) not in walls:
                    r += 1
        print(r, c)

if __name__ == '__main__':
    main()