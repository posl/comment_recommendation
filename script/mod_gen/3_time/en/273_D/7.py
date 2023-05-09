def main():
    #input
    HWRS = input().split()
    H = int(HWRS[0])
    W = int(HWRS[1])
    r_s = int(HWRS[2])
    c_s = int(HWRS[3])
    N = int(input())
    rcs = [input().split() for _ in range(N)]
    Q = int(input())
    dls = [input().split() for _ in range(Q)]
    
    #solve
    walls = set()
    for i in range(N):
        walls.add((int(rcs[i][0]), int(rcs[i][1])))
    r = r_s
    c = c_s
    for i in range(Q):
        d = dls[i][0]
        l = int(dls[i][1])
        if d == 'L':
            for j in range(l):
                if (r, c-1) not in walls:
                    c -= 1
        elif d == 'R':
            for j in range(l):
                if (r, c+1) not in walls:
                    c += 1
        elif d == 'U':
            for j in range(l):
                if (r-1, c) not in walls:
                    r -= 1
        elif d == 'D':
            for j in range(l):
                if (r+1, c) not in walls:
                    r += 1
        print(r, c)
    
    return

if __name__ == '__main__':
    main()