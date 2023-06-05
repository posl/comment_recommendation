def main():
    N, M = map(int, input().split())
    ab = []
    for i in range(M):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[0])
    #print(ab)
    res = [[] for i in range(N)]
    for i in range(M):
        res[ab[i][0]-1].append(ab[i][1])
        res[ab[i][1]-1].append(ab[i][0])
    #print(res)
    for i in range(N):
        res[i].sort()
        print(len(res[i]), end=' ')
        print(*res[i])
