def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P = [[sum(p), p[0], p[1], p[2]] for p in P]
    P.sort(reverse=True)
    for i in range(N):
        if P[i][0] + P[i][1] + P[i][2] + P[i][3] < P[K - 1][0]:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()