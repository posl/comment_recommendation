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

if __name__ == '__main__':
    main()