def main():
    N, K = map(int, input().split())
    P = [[0, 0, 0, 0] for i in range(N)]
    for i in range(N):
        P[i][0], P[i][1], P[i][2] = map(int, input().split())
        P[i][3] = P[i][0] + P[i][1] + P[i][2]
    P.sort(key=lambda x: x[3], reverse=True)
    for i in range(N):
        if P[i][3] + 300 * (3 - i) < P[K - 1][3]:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()