def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = []
    for i in range(N):
        r_i, c_i = map(int, input().split())
        walls.append((r_i, c_i))
    Q = int(input())
    moves = []
    for i in range(Q):
        d_i, l_i = input().split()
        moves.append((d_i, int(l_i)))
    for i in range(Q):
        d_i, l_i = moves[i]
        if d_i == 'L':
            for j in range(l_i):
                if (r_s, c_s - 1) in walls:
                    break
                else:
                    c_s -= 1
        elif d_i == 'R':
            for j in range(l_i):
                if (r_s, c_s + 1) in walls:
                    break
                else:
                    c_s += 1
        elif d_i == 'U':
            for j in range(l_i):
                if (r_s - 1, c_s) in walls:
                    break
                else:
                    r_s -= 1
        elif d_i == 'D':
            for j in range(l_i):
                if (r_s + 1, c_s) in walls:
                    break
                else:
                    r_s += 1
        print(r_s, c_s)
main()
