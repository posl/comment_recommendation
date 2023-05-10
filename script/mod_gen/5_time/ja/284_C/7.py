def main():
    N, M = map(int, input().split())
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    # 連結成分数を求める
    ans = 0
    # 連結成分数を求める
    ans = 0
    for i in range(M):
        # 辺 i を削除する
        # 連結成分数を求める
        visited = [False] * N
        visited[0] = True
        q = [0]
        while len(q) > 0:
            x = q.pop(0)
            for j in range(M):
                if u[j] == x:
                    if visited[v[j] - 1] == False:
                        visited[v[j] - 1] = True
                        q.append(v[j] - 1)
                if v[j] == x:
                    if visited[u[j] - 1] == False:
                        visited[u[j] - 1] = True
                        q.append(u[j] - 1)
        # 辺 i を追加する
        if visited[u[i] - 1] == False or visited[v[i] - 1] == False:
            ans += 1
        else:
            visited = [False] * N
            visited[0] = True
            q = [0]
            while len(q) > 0:
                x = q.pop(0)
                for j in range(M):
                    if u[j] == x:
                        if visited[v[j] - 1] == False:
                            visited[v[j] - 1] = True
                            q.append(v[j] - 1)
                    if v[j] == x:
                        if visited[u[j] - 1] == False:
                            visited[u[j] - 1] = True
                            q.append(u[j] - 1)
            if visited[u[i] - 1] == False or visited[v[i] - 1] == False:
                ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()