def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r_i, c_i = map(int, input().split())
        walls.add((r_i, c_i))
    Q = int(input())
    for _ in range(Q):
        d_i, l_i = input().split()
        l_i = int(l_i)
        if d_i == "L":
            for _ in range(l_i):
                if (r_s, c_s - 1) in walls:
                    break
                else:
                    c_s -= 1
        elif d_i == "R":
            for _ in range(l_i):
                if (r_s, c_s + 1) in walls:
                    break
                else:
                    c_s += 1
        elif d_i == "U":
            for _ in range(l_i):
                if (r_s - 1, c_s) in walls:
                    break
                else:
                    r_s -= 1
        else:
            for _ in range(l_i):
                if (r_s + 1, c_s) in walls:
                    break
                else:
                    r_s += 1
        print(r_s, c_s)

if __name__ == '__main__':
    main()