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

if __name__ == '__main__':
    main()