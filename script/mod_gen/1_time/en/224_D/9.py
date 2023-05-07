def main():
    import sys
    from collections import deque
    from copy import deepcopy
    from itertools import permutations
    input = sys.stdin.readline
    M = int(input())
    edge = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        edge[u-1].append(v-1)
        edge[v-1].append(u-1)
    a = list(map(int, input().split()))
    for i in range(8):
        a[i] -= 1
    q = deque()
    for i in range(8):
        q.append((i, a[i], 0))
    ans = -1
    while q:
        i, v, cnt = q.popleft()
        if i == 7:
            ans = cnt
            break
        for u in edge[v]:
            if u == a[i+1]:
                q.append((i+1, u, cnt))
            else:
                q.append((i, u, cnt+1))
    print(ans)

if __name__ == '__main__':
    main()