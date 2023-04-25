Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r, c = map(int, input().split())
        walls.add((r, c))
    Q = int(input())
    for _ in range(Q):
        d, l = input().split()
        l = int(l)
        for _ in range(l):
            if d == 'L':
                c_s -= 1
            elif d == 'R':
                c_s += 1
            elif d == 'U':
                r_s -= 1
            elif d == 'D':
                r_s += 1
            if (r_s, c_s) in walls:
                if d == 'L':
                    c_s += 1
                elif d == 'R':
                    c_s -= 1
                elif d == 'U':
                    r_s += 1
                elif d == 'D':
                    r_s -= 1
        print(r_s, c_s)

=======
Suggestion 2

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r, c = map(int, input().split())
        walls.add((r, c))
    Q = int(input())
    r = r_s
    c = c_s
    for _ in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for _ in range(l):
                if (r, c - 1) not in walls:
                    c -= 1
        elif d == 'R':
            for _ in range(l):
                if (r, c + 1) not in walls:
                    c += 1
        elif d == 'U':
            for _ in range(l):
                if (r - 1, c) not in walls:
                    r -= 1
        elif d == 'D':
            for _ in range(l):
                if (r + 1, c) not in walls:
                    r += 1
        print(r, c)

=======
Suggestion 3

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
        if d_i == 'L':
            c_s = max(1, c_s - l_i)
            while (r_s, c_s) in walls:
                c_s += 1
        elif d_i == 'R':
            c_s = min(W, c_s + l_i)
            while (r_s, c_s) in walls:
                c_s -= 1
        elif d_i == 'U':
            r_s = max(1, r_s - l_i)
            while (r_s, c_s) in walls:
                r_s += 1
        elif d_i == 'D':
            r_s = min(H, r_s + l_i)
            while (r_s, c_s) in walls:
                r_s -= 1
        print(r_s, c_s)

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    wall = set()
    for i in range(N):
        r, c = map(int, input().split())
        wall.add((r, c))
    Q = int(input())
    for i in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for j in range(l):
                if (r_s, c_s - 1) not in wall:
                    c_s -= 1
        elif d == 'R':
            for j in range(l):
                if (r_s, c_s + 1) not in wall:
                    c_s += 1
        elif d == 'U':
            for j in range(l):
                if (r_s - 1, c_s) not in wall:
                    r_s -= 1
        else:
            for j in range(l):
                if (r_s + 1, c_s) not in wall:
                    r_s += 1
        print(r_s, c_s)

=======
Suggestion 6

def solve():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    wall = set()
    for _ in range(N):
        r, c = map(int, input().split())
        wall.add((r, c))
    Q = int(input())
    d = {d: (dr, dc) for d, (dr, dc) in zip('LRUD', ((0, -1), (0, 1), (-1, 0), (1, 0)))}
    for _ in range(Q):
        di, l = input().split()
        dr, dc = d[di]
        l = int(l)
        for i in range(l):
            r_s += dr
            c_s += dc
            if (r_s, c_s) in wall:
                r_s -= dr
                c_s -= dc
                break
        print(r_s, c_s)

=======
Suggestion 7

def main():
    #input
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    rcs = [tuple(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    dls = [input().split() for _ in range(Q)]

    #compute
    d = {'L':(-1,0), 'R':(1,0), 'U':(0,1), 'D':(0,-1)}
    rcs = set(rcs)
    for i in range(Q):
        dl = dls[i]
        dl[1] = int(dl[1])
        for j in range(dl[1]):
            r_s += d[dl[0]][0]
            c_s += d[dl[0]][1]
            if (r_s, c_s) in rcs:
                r_s -= d[dl[0]][0]
                c_s -= d[dl[0]][1]

        #output
        print(r_s, c_s)

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    #input
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    rc = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    d_l = [list(input().split()) for _ in range(Q)]

    #compute
    d = {'L':(0,-1), 'R':(0,1), 'U':(-1,0), 'D':(1,0)}
    for i in range(Q):
        for j in range(int(d_l[i][1])):
            r_s, c_s = r_s + d[d_l[i][0]][0], c_s + d[d_l[i][0]][1]
            if [r_s, c_s] in rc:
                r_s, c_s = r_s - d[d_l[i][0]][0], c_s - d[d_l[i][0]][1]
        print(r_s, c_s)

=======
Suggestion 10

def  solve():
    h, w, r_s, c_s =  map ( int , input().split())
    n =  int (input())
    walls = set()
    for  _  in  range (n):
        r, c =  map ( int , input().split())
        walls.add((r, c))
    q =  int (input())
    d = { 'L' :(- 1 ,  0 ),  'R' :( 1 ,  0 ),  'U' :( 0 ,  1 ),  'D' :( 0 , - 1 )}
    for  _  in  range (q):
        di, l = input().split()
        l =  int (l)
        for  _  in  range (l):
            r_s += d[di][ 0 ]
            c_s += d[di][ 1 ]
            if  (r_s, c_s)  in  walls:
                r_s -= d[di][ 0 ]
                c_s -= d[di][ 1 ]
        print(r_s, c_s)
