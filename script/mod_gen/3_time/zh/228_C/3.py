def solve():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(tuple(map(int, input().split())))
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    for i in range(K):
        if P[i][0] + P[i][1] + P[i][2] < P[K - 1][0] + P[K - 1][1] + P[K - 1][2]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    solve()