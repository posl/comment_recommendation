def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        a, b = map(int, input().split())
        S.append((a, b))
    for i in range(N):
        c, d = map(int, input().split())
        T.append((c, d))
    S.sort()
    T.sort()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    dx = T[i][0] - S[j][0]
                    dy = T[i][1] - S[j][1]
                    dx2 = T[k][0] - S[l][0]
                    dy2 = T[k][1] - S[l][1]
                    if dx == dx2 and dy == dy2:
                        print('Yes')
                        return
    print('No')
    return

if __name__ == '__main__':
    main()