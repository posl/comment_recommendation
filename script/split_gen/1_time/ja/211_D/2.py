def main():
    #入力
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    #print(edge)
    #BFS
    q = [0]
    distance = [-1] * N
    distance[0] = 0
    cnt = [0] * N
    cnt[0] = 1
    while q:
        v = q.pop(0)
        for nv in edge[v]:
            if distance[nv] == -1:
                distance[nv] = distance[v] + 1
                q.append(nv)
                cnt[nv] = cnt[v]
            elif distance[nv] == distance[v] + 1:
                cnt[nv] = (cnt[nv] + cnt[v]) % (10**9+7)
    #print(distance)
    #print(cnt)
    #出力
    print(cnt[N-1])
