def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for _ in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    P = [x-1 for x in P]
    P_Y = sorted(zip(P, Y))
    P_Y = [list(x) for x in P_Y]
    P_Y = sorted(P_Y, key=lambda x: x[1])
    ans = [0]*M
    for i in range(M):
        ans[P_Y[i][0]] += 1
        print("{:06}{:06}".format(P_Y[i][0]+1, ans[P_Y[i][0]]))

if __name__ == '__main__':
    main()