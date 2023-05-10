def solve():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        P[i].append(sum(P[i]))
    P = sorted(P, key=lambda x: x[3], reverse=True)
    for i in range(N):
        if P[i][3] == P[K-1][3]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    solve()