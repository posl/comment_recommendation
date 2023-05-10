def get_input():
    h, w, rs, cs = map(int, input().split())
    n = int(input())
    walls = []
    for _ in range(n):
        walls.append(list(map(int, input().split())))
    q = int(input())
    instructions = []
    for _ in range(q):
        instructions.append(list(map(str, input().split())))
    return h, w, rs, cs, n, walls, q, instructions
