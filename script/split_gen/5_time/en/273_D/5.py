def get_input():
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
    return H, W, r_s, c_s, walls, Q, instructions
