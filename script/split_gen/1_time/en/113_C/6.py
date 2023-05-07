def main():
    N, M = [int(x) for x in input().split()]
    city = [tuple(int(x) for x in input().split()) for _ in range(M)]
    city.sort(key=lambda x: x[1])
    pref = [[] for _ in range(N)]
    for i in range(M):
        pref[city[i][0]-1].append(i)
    ans = [None] * M
    for i in range(N):
        for j in range(len(pref[i])):
            ans[pref[i][j]] = str(i+1).zfill(6) + str(j+1).zfill(6)
    print('
'.join(ans))
