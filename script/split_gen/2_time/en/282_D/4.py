def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    # print(G)
    ans = 0
    for i in range(N):
        # print(i)
        color = [-1]*N
        color[i] = 1
        que = deque([i])
        while que:
            v = que.popleft()
            for nv in G[v]:
                if color[nv] == -1:
                    color[nv] = 1 - color[v]
                    que.append(nv)
                else:
                    if color[nv] == color[v]:
                        break
            else:
                continue
            break
        else:
            ans += color.count(0)
            continue
        break
    else:
        print(ans)
        return
    print(0)
    return
