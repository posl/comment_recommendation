def main():
    n, m = map(int, input().split())
    d = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        d[a].append(b)
        d[b].append(a)
    visited = [False] * n
    visited[0] = True
    q = [0]
    ans = [0] * n
    while q:
        t = q.pop()
        for i in d[t]:
            if visited[i]:
                continue
            visited[i] = True
            ans[i] = t + 1
            q.append(i)
    print("Yes")
    for i in ans[1:]:
        print(i)

if __name__ == '__main__':
    main()