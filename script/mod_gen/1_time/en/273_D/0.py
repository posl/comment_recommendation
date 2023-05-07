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

if __name__ == '__main__':
    main()