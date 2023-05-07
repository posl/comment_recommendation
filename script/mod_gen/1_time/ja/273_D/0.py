def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    blocks = [tuple(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    instructions = [tuple(input().split()) for _ in range(Q)]
    blocks = set(blocks)
    for d, l in instructions:
        for _ in range(int(l)):
            if d == 'L':
                c_s -= 1
            elif d == 'R':
                c_s += 1
            elif d == 'U':
                r_s -= 1
            elif d == 'D':
                r_s += 1
            if (r_s, c_s) in blocks:
                if d == 'L':
                    c_s += 1
                elif d == 'R':
                    c_s -= 1
                elif d == 'U':
                    r_s += 1
                elif d == 'D':
                    r_s -= 1
                break
        print(r_s, c_s)
main()

if __name__ == '__main__':
    main()