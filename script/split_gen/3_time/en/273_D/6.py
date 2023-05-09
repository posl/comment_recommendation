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
