def main():
    M = int(input())
    if M == 0:
        print(0)
        return
    edges = [list(map(int, input().split())) for _ in range(M)]
    p = list(map(int, input().split()))
    a = [0] * 9
    for i in range(8):
        a[p[i] - 1] = i + 1
    a[8] = 9
    # print(a)
    graph = [[0] * 9 for _ in range(9)]
    for u, v in edges:
        graph[u - 1][v - 1] = 1
        graph[v - 1][u - 1] = 1
    # print(graph)
    ans = 10 ** 10
    for i in range(9):
        for j in range(9):
            for k in range(9):
                for l in range(9):
                    for m in range(9):
                        for n in range(9):
                            for o in range(9):
                                for q in range(9):
                                    for r in range(9):
                                        b = [i, j, k, l, m, n, o, q, r]
                                        if sorted(b) != list(range(9)):
                                            continue
                                        # print(b)
                                        c = [0] * 9
                                        for s in range(9):
                                            c[b[s]] = a[s]
                                        # print(c)
                                        d = [0] * 9
                                        for s in range(9):
                                            d[s] = c[s]
                                        # print(d)
                                        cnt = 0
                                        for s in range(8):
                                            if d[s] != s + 1:
                                                cnt += 1
                                                t = d.index(s + 1)
                                                d[t], d[s] = d[s], d[t]
                                        # print(d)
                                        ans = min(ans, cnt)
    if ans == 10 ** 10:
        print(-1)
    else:
        print(ans)
