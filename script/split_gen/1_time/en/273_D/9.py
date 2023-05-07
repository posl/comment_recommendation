def get_input():
    H, W, r_s, c_s = [int(x) for x in input().split()]
    N = int(input())
    walls = set()
    for _ in range(N):
        r, c = [int(x) for x in input().split()]
        walls.add((r, c))
    Q = int(input())
    instructions = []
    for _ in range(Q):
        d, l = input().split()
        instructions.append((d, int(l)))
    return H, W, r_s, c_s, walls, Q, instructions
