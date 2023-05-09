def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = []
    for i in range(N):
        r, c = map(int, input().split())
        walls.append((r, c))
    Q = int(input())
    instructions = []
    for i in range(Q):
        d, l = input().split()
        instructions.append((d, int(l)))
    #print(H, W, r_s, c_s, N, walls, Q, instructions)
    for d, l in instructions:
        if d == 'L':
            c_s = max(1, c_s - l)
        elif d == 'R':
            c_s = min(W, c_s + l)
        elif d == 'U':
            r_s = max(1, r_s - l)
        elif d == 'D':
            r_s = min(H, r_s + l)
        print(r_s, c_s)
main()

if __name__ == '__main__':
    main()