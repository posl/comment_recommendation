def main():
    M = int(input())
    edge = [list(map(int, input().split())) for _ in range(M)]
    pos = list(map(int, input().split()))
    G = [[] for _ in range(10)]
    for u, v in edge:
        G[u].append(v)
        G[v].append(u)
    for i in range(10):
        G[i].sort()
    ans = 100
    for i in range(8):
        for j in range(i + 1, 8):
            if pos[i] == pos[j]:
                print(-1)
                exit()
    for i in range(8):
        for j in range(i + 1, 8):
            for k in range(j + 1, 8):
                for l in range(k + 1, 8):
                    for m in range(l + 1, 8):
                        for n in range(m + 1, 8):
                            for o in range(n + 1, 8):
                                for p in range(o + 1, 8):
                                    now = [pos[i], pos[j], pos[k], pos[l], pos[m], pos[n], pos[o], pos[p]]
                                    cnt = 0
                                    for q in range(8):
                                        if now[q] != q + 1:
                                            cnt += 1
                                    if cnt >= ans:
                                        continue
                                    for q in range(8):
                                        if now[q] != q + 1:
                                            break
                                    now[q] = 0
                                    while 0 in now:
                                        if now.count(0) == 1:
                                            break
                                        for r in range(8):
                                            if now[r] == 0:
                                                break
                                        flag = False
                                        for s in G[r + 1]:
                                            if now[s - 1] != 0:
                                                now[r] = now[s - 1]
                                                now[s - 1] = 0
                                                flag = True
                                                break
                                        if not flag:
                                            break
                                    if now == [1, 2, 3, 4, 5, 6, 7, 8]:
                                        ans = min(ans, cnt)
    if ans == 100:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()