def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    wall = set()
    for n in range(N):
        r_i, c_i = map(int, input().split())
        wall.add((r_i, c_i))
    Q = int(input())
    for q in range(Q):
        d_i, l_i = input().split()
        l_i = int(l_i)
        if d_i == 'L':
            for i in range(l_i):
                c_s -= 1
                if (r_s, c_s) in wall:
                    c_s += 1
                    break
        elif d_i == 'R':
            for i in range(l_i):
                c_s += 1
                if (r_s, c_s) in wall:
                    c_s -= 1
                    break
        elif d_i == 'U':
            for i in range(l_i):
                r_s -= 1
                if (r_s, c_s) in wall:
                    r_s += 1
                    break
        elif d_i == 'D':
            for i in range(l_i):
                r_s += 1
                if (r_s, c_s) in wall:
                    r_s -= 1
                    break
        print(r_s, c_s)

if __name__ == '__main__':
    main()