def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N)]
    for A, B in AB:
        A -= 1
        B -= 1
        G[A].append(B)
    ans = []
    done = [False] * N
    for i in range(N):
        if done[i]:
            continue
        done[i] = True
        stack = [i]
        while stack:
            v = stack.pop()
            ans.append(v)
            for nv in G[v]:
                if done[nv]:
                    print(-1)
                    return
                done[nv] = True
                stack.append(nv)
    print(*[v + 1 for v in ans])
main()
