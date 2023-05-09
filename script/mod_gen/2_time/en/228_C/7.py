def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        P[i].sort()
        P[i].reverse()
    P.sort()
    P.reverse()
    for i in range(N):
        if P[i][0] + P[i][1] + P[i][2] + P[i][3] >= P[K-1][0] + P[K-1][1] + P[K-1][2] + P[K-1][3]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()