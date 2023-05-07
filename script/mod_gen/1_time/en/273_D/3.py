def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r_i, c_i = map(int, input().split())
        walls.add((r_i, c_i))
    Q = int(input())
    instructions = []
    for _ in range(Q):
        d_i, l_i = input().split()
        instructions.append((d_i, int(l_i)))
    for d_i, l_i in instructions:
        if d_i == 'L':
            for _ in range(l_i):
                c_s -= 1
                if (r_s, c_s) in walls:
                    c_s += 1
                    break
        elif d_i == 'R':
            for _ in range(l_i):
                c_s += 1
                if (r_s, c_s) in walls:
                    c_s -= 1
                    break
        elif d_i == 'U':
            for _ in range(l_i):
                r_s -= 1
                if (r_s, c_s) in walls:
                    r_s += 1
                    break
        else:
            for _ in range(l_i):
                r_s += 1
                if (r_s, c_s) in walls:
                    r_s -= 1
                    break
        print(r_s, c_s)

if __name__ == '__main__':
    main()